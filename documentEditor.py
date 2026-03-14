from abc import ABC, abstractmethod

class Document:
  def __init__(self,elements):
    self.elements = [None]
  
  def addElement(self,element):
    self.elements.append(element)

class DocumentEditor:
  def __init__(self,persistance):
    self.persistance = persistance
    
  def saveDocument(self,document):
    self.persistance.save(document)
  
   
class Persistance(ABC):
  @abstractmethod
  def save(self,document):
    pass

class saveToFile(Persistance):
  def save(self,document):
    print("Saving to file")

class saveToCloud(Persistance):
  def save(self,document):
    print("Saving to cloud")

class DocumentElement(ABC):
  @abstractmethod
  def render(self):
    pass
    
class TextElement(DocumentElement):
  def __init__(self,text):
    self.text = text
    
  def render(self):
    print(f"Rendering text: {self.text}")

class ImageElement(DocumentElement):
  def __init__(self,imagePath):
    self.imagePath = imagePath
    
  def render(self):
    print(f"Rendering image from: {self.imagePath}")


    
    