class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  
  def start_engine(self):
    print("Engine started.")
  
  def stop_engine(self):
    print("Engine stopped.")
    
class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
  
  def start_engine(self):
    print("Electric car engine started.")
  
  def stop_engine(self):
    print("Electric car engine stopped.")
    
class ManualCar(Car):
  def __init__(self, make, model, year, gear_count):
    super().__init__(make, model, year)
    self.gear_count = gear_count
  
  def start_engine(self):
    print("Manual car engine started.")
  
  def stop_engine(self):
    print("Manual car engine stopped.")

