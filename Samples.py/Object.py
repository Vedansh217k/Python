class car :
    total = 0
    def __init__(self, brand , model):
        self.__brand  = brand
        self.__model  = model
        car.total += 1
    def get_brand(self):
        return self.__brand + " !"
    
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "petrol , diesel"
    @staticmethod    
    def general_description():
        return " cars are a means of transport"
    
    @property   
    def model(self):
        return self.__model

class electriccar(car):

    def __init__(self, brand,model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 
    def fuel_type(self):
        return "electric charge"

my_tesla = electriccar("Tesla" , "Model S" , "85kwh")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())
safari = car("Tata","safari")
# safari.model ="City"


print(safari.fuel_type())
print(safari.total)

# print(safari.general_description())
print(car.general_description())

print(safari.model)
# my_car = car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = car("Tata" , "Safari")
# print(my_new_car.model)
class Battery:
    def battery_info(self):
        return " this is battery"
    
class Engine:
    def engine_info(self):
        return "this is engine"
    
class ElectricCar(Battery,Engine,car):
     pass  

my_new_tesla = ElectricCar("Tesla" , "Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
