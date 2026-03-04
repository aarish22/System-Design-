##  dependency inversion principle
# high-level modules should not depend on low-level modules. Both should depend on abstractions.
# abstractions should not depend on details. Details should depend on abstractions. 

from abc import ABC, abstractmethod

class Application:
  def __init__(self,db):
    self.db = db
    
  def saveData(self):
    return self.db.save()
  
class Database(ABC):
  @abstractmethod
  def save(self):
    pass
  
class MySQLDatabase(Database):
  def save(self):
    return "Data saved to MySQL Database"

class MongoDB(Database):
  def save(self):
    return "Data saved to MongoDB Database"
  
mysql_db = MySQLDatabase()
app = Application(mysql_db)
print(app.saveData())
mongo_db = MongoDB()
app = Application(mongo_db)
print(app.saveData())