## Class Invariant is a condition that must always be true for an object of a class. It is a rule that defines the valid state of an object and ensures that the object remains in a consistent and valid state throughout its lifetime. If a child class violates the invariant of its parent class, it can lead to unexpected behavior and errors in the program. Therefore, it is important for child classes to adhere to the invariants defined by their parent classes to maintain the integrity of the object and ensure that it behaves as expected. In simple words suppose in account class we have invariant that balance should never be negative, if we create a child class that violates this invariant by allowing negative balance, it can lead to issues in the program when we try to perform operations on the account object. Therefore, it is important for child classes to follow the invariants defined by their parent classes to ensure that the objects remain in a valid state and behave as expected.

class Account:
  def __init__(self):
    self._balance = 0

  @property   ## getter method to access the balance attribute
  def balance(self):
    return self._balance
  
  
  @balance.setter  ## setter method to set the balance attribute
  def balance(self, value):
    if value < 0:
      raise ValueError("Balance cannot be negative")
    self._balance = value

  def checkInvariant(self):
    if self._balance < 0:
      raise ValueError("Balance cannot be negative")


class CheatAccount(Account):
  def __init__(self):
    super().__init__()
    self.balance = -100  ## violates the invariant of parent class because balance cannot be negative
    
account = CheatAccount()  ## this will raise an error because balance cannot be negative


## history constraint is a rule that states that a child class should not change the history of the parent class. This means that if a parent class has a certain behavior or state, the child class should not change it in a way that would affect the behavior or state of the parent class. For example, if a parent class has a method that updates a certain attribute, the child class should not override that method in a way that would change the behavior of the parent class. This is important because it ensures that the child class can be used in place of the parent class without causing any unexpected behavior or errors. If a child class violates the history constraint, it can lead to issues in the program when we try to use the child class in place of the parent class. Therefore, it is important for child classes to follow the history constraint defined by their parent classes to ensure that the objects remain in a valid state and behave as expected. For example let us take a account class that has a method to update the balance, if we create a child class that overrrides that method to  do cheating by adding some amount to the balance, it will violate the history constraint because it will change the behavior of the parent class and can lead to issues in the program when we try to use the child class in place of the parent class. Therefore, it is important for child classes to follow the history constraint defined by their parent classes to ensure that the objects remain in a valid state and behave as expected.
class Account:
  def __init__(self):
    self._balance = 0

  @property   ## getter method to access the balance attribute
  def balance(self):
    return self._balance
  
  
  @balance.setter  ## setter method to set the balance attribute
  def balance(self, value):
    if value < 0:
      raise ValueError("Balance cannot be negative")
    self._balance = value

  def updateBalance(self, amount):
    self.balance += amount
    
class CheatAccount(Account):
  def __init__(self):
    super().__init__()
  
  def updateBalance(self, amount):
    self.balance += amount + 100  ## violates the history constraint of parent class because it changes the behavior of the parent class by adding some amount to the balance