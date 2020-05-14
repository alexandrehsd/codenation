from datetime import datetime

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


def add_diff_in_sec(records):
    """
    Add time difference and convert time stamps to datetime objects
    """

    for record in records:
        record['end'] = datetime.fromtimestamp(record['end'])
        record['start'] = datetime.fromtimestamp(record['start'])

        record['diff_in_sec'] = (record['end'] - record['start']).seconds

    return(records)

def add_default_tax(records):
    """
    Add tax per minute info of the call
    """

    for record in records:
        record['tax_per_min'] = (0.09 if record['start'].hour >= 6 and record['start'].hour <= 22 else 0)

    return(records)

def classify_by_phone_number(records):
    records = add_diff_in_sec(records)
    records = add_default_tax(records)
    
    return(records)    
    

# print(classify_by_phone_number(records))



    

