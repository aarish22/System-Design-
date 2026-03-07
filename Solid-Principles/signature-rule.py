
## method argumnet rule
class Animal:
  def __init__(self,name,diet):
    self.name = name
    self.diet = diet
  
  def sound(self,s: str):
    pass

class Dog(Animal):
  def __init__(self,name,diet):
    super().__init__(name,diet)
  
  def sound(self, s: str):  ## <-- same method argumment as parent
    return f"Bark!"
    
## return type rule
class organism:
  pass

class plant:
  pass

class Factory:
  def create(self) -> organism:
    return organism()

class PlantFactory(Factory):
  def create(self) -> plant:  ## same or narrower(child) return type 
    return plant()
  
## exception rule

class Payment:
    def pay(self, amount):
        raise ValueError("Invalid amount")

class CryptoPayment(Payment):
    def pay(self, amount):
        raise Exception("System crash")  # should be same or narrower exception return type
      

## precondition rule
class Vehicle:  
    def start(self, fuel):
        if fuel <= 0:
            raise ValueError("Fuel must be greater than zero")
        return "Vehicle started"  
      
class Car(Vehicle):
    def start(self, fuel):
        if fuel <= 0:
            raise ValueError("Fuel must be greater than zero")  # same or weaker precondition
        return "Car started"
      
## postcondition rule
class Account:
    def get_balance(self):
        return 1000 
class SavingsAccount(Account):
    def get_balance(self):
        balance = super().get_balance()
        return balance  # same or stronger postcondition
