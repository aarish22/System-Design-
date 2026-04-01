
## Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In other words, if class B is a subclass of class A, then we should be able to replace A with B without breaking the functionality of the program. This principle is important for ensuring that our code is flexible and maintainable, as it allows us to use polymorphism and inheritance effectively.

class DepositAcc(ABC):
  @abstractmethod
  def deposit(self,amt):
    pass

class WithdrawableAcc(DepositAcc):
  @abstractmethod
  def withdraw(self,amt):
    pass 
  
  
class CurrentAccount(WithdrawableAcc):
  def __init__(self):
    self.balance = 0
  
  def deposit(self, amt):
    self.balance += amt
    return f"Deposited Rs.{amt}"
  
  def withdraw(self, amt):
    if self.balance >= amt:
      self.balance -= amt
      return f"Rs. {amt} has been withdrawn"
    return f"Insufficient Balance"

class FixedTermAccount(DepositAcc):
  def __init__(self):
    self.balance = 0
    self.isDeposited = False
  
  def deposit(self, amt):
    if self.isDeposited:
      return f"Deposit already made. Cannot deposit again"  
    self.balance += amt
    self.isDeposited = True
    return f'Amount of Rs. {amt} has been succesfully deposited'
     
    