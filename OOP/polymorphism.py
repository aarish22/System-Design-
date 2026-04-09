## dynamic polymorphism - also called method overriding
## It allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the method in the superclass, and when the method is called on an instance of the subclass, the overridden method is executed.
## method signature - the method name and the number and type of parameters it accepts. In method overloading, the method signature is used to determine which method to execute based on the arguments passed to the method. In method overriding, the method signature is the same in both the superclass and subclass, but the implementation is different in the subclass.

## In the example below, we have a base class `Animal` with a method `make_sound()`. The subclasses `Dog` and `Cat` override this method to provide their specific implementations.

## static polymorphism - also called method overloading
## It allows a class to have multiple methods with the same name but different parameters. The method that is executed is determined at compile time based on the number and type of arguments passed to the method.

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  
  def start_engine(self):
    print("Engine started.")
  
  def stop_engine(self):
    print("Engine stopped.")
  
  def accelerate(self, speed):
    pass   
    
class ElectricCar(Car):
  def start_engine(self):
    print("Electric car engine started.")
  def stop_engine(self):
    print("Electric car engine stopped.")
  def accelerate(self, speed, mode="normal"):
    if mode == "sport":
      print(f"Electric car accelerating to {speed} mph in sport mode.")
    else:
      print(f"Electric car accelerating to {speed} mph in normal mode.")

class GasolineCar(Car):
  def start_engine(self):
    print("Gasoline car engine started.")
  def stop_engine(self):
    print("Gasoline car engine stopped.")
  def accelerate(self, speed):
    print(f"Gasoline car accelerating to {speed + 20} mph.")


tesla = ElectricCar("Tesla", "Model S", 2020)
toyota = GasolineCar("Toyota", "Camry", 2019)

tesla.start_engine()  # Output: Electric car engine started.
toyota.start_engine()  # Output: Gasoline car engine started.

tesla.accelerate(60)  # Output: Electric car accelerating to 60 mph in normal mode.
tesla.accelerate(60, mode="sport")  # Output: Electric car accelerating to 60 mph in sport mode.

toyota.accelerate(60)  # Output: Gasoline car accelerating to 80 mph.
tesla.stop_engine()  # Output: Electric car engine stopped.
toyota.stop_engine()  # Output: Gasoline car engine stopped.

