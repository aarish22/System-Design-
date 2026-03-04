## strong "has-a" relationship
## One object completely owns another object.
# If the parent object is destroyed, the child object is also destroyed.

class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()   # created inside → composition
    
    def start_car(self):
        return self.engine.start()

c1 = Car()
print(c1.start_car())

"""
class Car:
    def __init__(self, engine):
        self.engine = engine   # passed from outside
"""

"""
class Car:
    def __init__(self, engine):
        self.engine = engine   # passed from outside
"""