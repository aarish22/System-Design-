from abc import ABC,abstractmethod
import random
class Bank(ABC):
  def __init__(self,name,branch):
    self.name = name
    self.branch = branch
  
  @abstractmethod
  def open_acc(self): ## abstract method
    pass
  
  @abstractmethod
  def close_acc(self): ## abstract method
    pass
  
  @abstractmethod
  def balance(self):
    pass
  
  @abstractmethod
  def deposit(self,amt:int):
    pass
  
  @abstractmethod
  def withdraw(self,amt:int):
    pass

class SBI(Bank):
  def __init__(self, name, branch):
    super().__init__(name, branch)
    self._balance = 0
    self.acc_no = random.randrange(10000000,99999999)
    
  def open_acc(self):
    return f"Your SBI account has been opened"

  def close_acc(self):
    return f"Your SBI account having {self.acc_no} has been closed"

  def balance(self):
    return f"Your current balance is {self._balance}"
  
  def deposit(self, amt):
    self._balance += amt
    print(f"{amt} has been deposited to your account")

  def withdraw(self, amt):
    if self._balance >= amt:
      self._balance -= amt
      print(f"Rs. {amt} has been successfully withdrawn") 
    return f"Insufficient Balance"   
    
  