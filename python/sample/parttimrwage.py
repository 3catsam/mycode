class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self,hours):
        self.hours=hours
        return super(PartTimeEmployee,self).calculate_wage(hours)
#milton is a instance name.
milton=PartTimeEmployee("Sam")
print milton.full_time_wage(10)
print milton.employee_name