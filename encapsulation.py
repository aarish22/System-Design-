## Encapsulation deals with data security while abstraction deals with data hiding
## Encapsulation is the process of wrapping data and methods that operate on the data within a single unit, such as a class. It helps to protect the data from unauthorized access and modification by restricting access to the internal state of the object.
## Access modifiers are used to define the visibility of class members. In Python, we use a single underscore (_) to indicate that a member is intended for internal use (protected) and a double underscore (__) to indicate that a member is private.

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.__engine_status = "off"  # Private attribute
  
  def start_engine(self):
    self.__engine_status = "on"
    print("Engine started.")
  
  def stop_engine(self):
    self.__engine_status = "off"
    print("Engine stopped.")
  
  def get_engine_status(self):
    return self.__engine_status  # Public method to access private attribute

car = Car("Honda", "Civic", 2021)
car.start_engine()  # Output: Engine started.
print(car.get_engine_status())  # Output: on
car.stop_engine()  # Output: Engine stopped.
print(car.get_engine_status())  # Output: off
# Attempting to access private attribute directly will result in an error
# print(car.__engine_status)  # This will raise an AttributeError 