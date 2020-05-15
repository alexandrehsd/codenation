from datetime import datetime
import pdb
records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def get_diff_in_sec(record):
    """
    get time difference and convert time stamps to datetime objects
    Input: Call information (dict)
    """

    end = datetime.fromtimestamp(record['end'])
    start = datetime.fromtimestamp(record['start'])
    diff_in_sec = (end - start).seconds

    return(diff_in_sec)

def rm_invalid(records):
    """
    Remove invalid calls which are calls that starts in a day and end in the next one
    """

    for index, record in enumerate(records):
        start_day = datetime.fromtimestamp(record['start']).day
        end_day = datetime.fromtimestamp(record['end']).day

        if(start_day != end_day):
            records[index].pop()

    return(records)

def calc_default_tax(record):
    """
    Calculate tax per minute info of the call
    """

    start_dttime = datetime.fromtimestamp(record['start']).hour
    end_dttime = datetime.fromtimestamp(record['end']).hour

    tax_per_min = (0.09 if (start_dttime >= 6) and (start_dttime <= 22) else 0)

    return(tax_per_min)

def calc_call_price(diff_in_sec, tax_per_min):
    """
    Calculate the total cost of the call
    """

    call_minutes = diff_in_sec // 60
    total = 0.36 + call_minutes*tax_per_min

    return(total)

def classify_by_phone_number(records):
    records = rm_invalid(records)

    results = []
    for record in records:
        diff_in_sec = get_diff_in_sec(record)
        tax_per_min = calc_default_tax(record)

        call_price = calc_call_price(diff_in_sec, tax_per_min)

        # If there is no register of the source number in the calls list
        # then append a record for that source in the results list
        if not any(record['source'] in result['source'] for result in results):
            results.append({'source': record['source'], 'total': call_price})
        else:
            for call in results:
                if(call['source'] == record['source']):
                    call['total'] += call_price

    for result in results:
        result['total'] = round(result['total'], 2)
        
    results = sorted(results, key = lambda k: k['total'], reverse = True)

    return(results)