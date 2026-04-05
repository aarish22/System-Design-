## document editor helper class with support for adding text and images, saving to different storage options, and rendering the document elements. The design follows the Open/Closed Principle, allowing for easy extension of new element types and persistence methods without modifying existing code.

## The Document class represents the document being edited, while the DocumentEditor class provides methods for adding elements, saving, and rendering. The Persistence interface defines the contract for saving documents, and concrete implementations like SaveToFile and SaveToCloud provide specific saving behavior. The DocumentElement interface allows for different types of elements (text and images) to be added to the document, each with its own rendering logic.


from abc import ABC, abstractmethod

class Document:
    def __init__(self):
        self.elements = []

    def addElement(self, element):
        self.elements.append(element)


class DocumentEditor:
    def __init__(self, document, persistence):
        self.document = document
        self.persistence = persistence

    def addImage(self, imagePath):
        imageElement = ImageElement(imagePath)
        self.document.addElement(imageElement)

    def addText(self, text):
        textElement = TextElement(text)
        self.document.addElement(textElement)

    def saveDocument(self):
        self.persistence.save(self.document)

    def renderDocument(self):
        for element in self.document.elements:
            element.render()


class Persistence(ABC):
    @abstractmethod
    def save(self, document):
        pass


class SaveToFile(Persistence):
    def save(self, document):
        print("Saving to file")


class SaveToCloud(Persistence):
    def save(self, document):
        print("Saving to cloud")


class DocumentElement(ABC):
    @abstractmethod
    def render(self):
        pass


class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(f"Rendering text: {self.text}")


class ImageElement(DocumentElement):
    def __init__(self, imagePath):
        self.imagePath = imagePath

    def render(self):
        print(f"Rendering image from: {self.imagePath}")

class Client:
    def main(self):
        document = Document()
        persistence = SaveToFile()
        editor = DocumentEditor(document, persistence)

        editor.addText("Hello, World!")
        editor.addImage("/path/to/image.png")
        editor.saveDocument()
        editor.renderDocument()

if __name__ == "__main__":
    client = Client()
    client.main() 
