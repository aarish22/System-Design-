## interface segregation principle --# states that a client should not be forced to implement an interface that it doesn't use. This means that if a class implements an interface, it should only implement the methods that are relevant to its functionality and not be forced to implement methods that it doesn't need. For example, if we have an interface for a shape that has methods for calculating area and perimeter, a class that implements this interface should only implement the methods that are relevant to its functionality. If we create a class for a circle that implements the shape interface, it should only implement the method for calculating the area and not be forced to implement the method for calculating the perimeter, because a circle does not have a perimeter. If we create a class for a rectangle that implements the shape interface, it should implement both methods for calculating the area and perimeter, because a rectangle has both an area and a perimeter. Therefore, it is important for classes to follow the interface segregation principle to ensure that they only implement the methods that are relevant to their functionality and do not implement methods that they don't need, which can lead to cleaner and more maintainable code. (circle has circumeference instead of perimeter but we can ignore that for simplicity)

from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
  
  @abstractmethod
  def perimeter(self):
    pass
  
  
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return 3.14 * self.radius ** 2
  
  def perimeter(self):
    raise NotImplementedError("Circle does not have a perimeter")

class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2 * (self.length + self.width)
circle = Circle(5)
print(circle.area())    

rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())


## correct implementation of interface segregation principle by creating separate interfaces for area and perimeter

from abc import ABC, abstractmethod
class Area(ABC):
  @abstractmethod
  def area(self):
    pass
class Perimeter(ABC):
  @abstractmethod
  def perimeter(self):
    pass
class Circle(Area):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return 3.14 * self.radius ** 2

class Rectangle(Area, Perimeter):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2 * (self.length + self.width)
circle = Circle(5)
print(circle.area())    
rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())


## 2d shape interface and 3d shape interface

from abc import ABC, abstractmethod
class Shape2D(ABC): 
  @abstractmethod
  def area(self):
    pass

class Shape3D(ABC):
  @abstractmethod
  def volume(self):
    pass
  
class Square(Shape2D):
  def __init__(self, side):
    self.side = side
  
  def area(self):
    return self.side ** 2

class Cube(Shape3D):
  def __init__(self, side):
    self.side = side
  
  def volume(self):
    return self.side ** 3

square = Square(4)
print(square.area())
cube = Cube(3)
print(cube.volume())