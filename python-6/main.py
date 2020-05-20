class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

class Employee:
    def __new__(cls, code, name, salary):
        instance = super(Employee, cls).__new__(cls)
        if isinstance(instance, Manager) or isinstance(instance, Seller):
            return instance
        else:
            raise TypeError("You cannot instantiate an object of class Employee directly")

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def get_hours(self):
        return 8

    def calc_bonus(self):
        return self.salary * 0.15

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def get_department(self):
        return self._departament

    def set_department(self, dept_name):
        self._departament.set_name(dept_name)

class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, sale):
        self._sales += sale

    def calc_bonus(self):
        return self._sales * 0.15