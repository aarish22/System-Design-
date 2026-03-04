## inheritance(is-a relationship)
 
class Animal:
  def __init__(self,name):
    self.name = name
  
  
  def describe(self):
    return f"{self.name} is an animal"
  
class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)
    
  def describe(self):
    return super().describe() +" specifically a dog"
  
bahadur = Dog("Bahadur")
print(bahadur.describe())

print(Dog.__mro__)

