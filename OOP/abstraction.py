## Abstraction is the process of hiding the implementation details and showing only functionality to the user. It helps to reduce complexity and allows the user to interact with the system without knowing the internal workings.
class Car:
  def _init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year  
  def start_engine(self):
    pass
  def stop_engine(self):
    pass

class ElectricCar(Car):
  def start_engine(self):
    print("Electric car engine started.")
  def stop_engine(self):
    print("Electric car engine stopped.")

class GasolineCar(Car):
  def start_engine(self):
    print("Gasoline car engine started.")
  def stop_engine(self):
    print("Gasoline car engine stopped.")
    
# Example usage
electric_car = ElectricCar("Tesla", "Model S", 2020)
gasoline_car = GasolineCar("Toyota", "Camry", 2019)
electric_car.start_engine()  # Output: Electric car engine started. 
gasoline_car.start_engine()  # Output: Gasoline car engine started.
