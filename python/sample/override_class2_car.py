class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %d MPG." % (self.color,self.model,self.mpg)
    def drive_car(self):
        self.condition="used"
class ElectricCar(Car):
    def __init__(self,model, color, mpg,battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type=battery_type
    def drive_car(self):
        self.condition="like new"
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.display_car()

my_car.drive_car()
print my_car.condition

my_car=ElectricCar("volvo", "silver", 88,"molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition
my_car.display_car()