## pre condition -- a condition that must be true before a method is executed. It is a requirement that must be met in order for the method to work correctly. For example, if we have a method that calculates the area of a rectangle, the pre condition would be that the length and width of the rectangle must be positive numbers. If we create a child class that violates this pre condition by allowing negative numbers for length and width, it can lead to issues in the program when we try to calculate the area of the rectangle. Therefore, it is important for child classes to follow the pre conditions defined by their parent classes to ensure that the methods work correctly and produce expected results.

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def area(self):
    if self.length <= 0 or self.width <= 0:  ## pre condition that length and width must be positive numbers
      raise ValueError("Length and width must be positive numbers")
    return self.length * self.width
  
class CheatRectangle(Rectangle):
  def __init__(self, length, width):
    super().__init__(length, width)
  
  def area(self):
    return self.length * self.width  ## violates the pre condition of parent class because it does not check for negative numbers for length and width
  
rect = CheatRectangle(-5, 10)
print(rect.area())  ## this will not raise an error because it does not check for negative numbers for length and width, but it will produce an incorrect result of -50 instead of 50 


##post condition -- suppose a car class has break method when which when called reduces speed by , a subclass/child class of car class should also have the same post condition that when break method is called it should reduce the speed by 10 plus we can add some extra functionality like increase charge by 10 but it should not change the post condition of parent class which is to reduce the speed by 10, if we create a child class that violates this post condition by not reducing the speed by 10 when the break method is called, it can lead to issues in the program when we try to use the child class in place of the parent class. Therefore, it is important for child classes to follow the post conditions defined by their parent classes to ensure that the methods work correctly and produce expected results.

class Car:
  def __init__(self):
    self.speed = 100
  
  def breaks(self):
    self.speed -= 10  ## post condition that when break method is called it should reduce the speed by 10

class ElectricCar(Car):
  def __init__(self):
    super().__init__()
    self.charge = 100
  
  def breaks(self):
    self.speed -= 10  ## same post condition as parent class that when break method is called it should reduce the speed by 10
    self.charge -= 10  ## extra functionality to reduce charge by 10 when break method is called