
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