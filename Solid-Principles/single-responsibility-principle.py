class Product:
  def __init__(self,name,price):
    self.name = name
    self.price = price

class ShoppingCart:
  def __init__(self):
    self.totalProducts = []
    
  def pushProduct(self,product):
    self.totalProducts.append(product)
    
  def getPrice(self):
    return sum(product.price for product in self.totalProducts)
  
  
class Invoice:
  def __init__(self,cart):
    self.cart = cart
    
  def generate(self):
    return f"Rs. {self.cart.getPrice()} - Invoice generated "
    
  
class SavetoDB:
  def __init__(self,cart):
    self.cart = cart
  
  def save(self):
    return f"{len(self.cart.totalProducts)} - products saved to Db"
    
    
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 15000)

cart = ShoppingCart()
cart.pushProduct(p1)
cart.pushProduct(p2)

invoice = Invoice(cart)
print(invoice.generate())

db = SavetoDB(cart)
print(db.save())