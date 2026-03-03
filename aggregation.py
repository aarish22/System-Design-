### has-a relationship, One object stores another object as a part, can exists independently

class Teacher:
    __slots__= ['name']
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Teacher : {self.name}"

class Student:
  def __init__(self, name, teacher):
      self.name = name
      self.teacher = teacher   # aggregation
  
  def get_teacher_name(self):
      return self.teacher.name
    
teacher1 = Teacher("nesta")
student1 = Student("ronaldo",teacher1)
del teacher1

print(student1.name)
###print(teacher1.name)