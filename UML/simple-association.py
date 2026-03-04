## object-association -- just related
## If a class uses __slots__, then dynamic attributes are NOT allowed, else dynamic attributes are allowed in python
## __slots__ =['name']
class Teacher:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Teacher : {self.name}"


class Student:
    def __init__(self, name):
        self.name = name
    

teacher1 = Teacher("Rajni")
student1 = Student("Asasuka")

student1.teacher = teacher1   # association
print(student1.teacher)
print(student1.__dict__)

""" student1  ───────→  Student object
                       name = "asasuka"
                       teacher ───→ teacher1 object

teacher1 ───────→  Teacher object
                       name = "Rajni" """
                       
## Creating a new attribute teacher inside the student1 object
## Storing a reference to teacher1