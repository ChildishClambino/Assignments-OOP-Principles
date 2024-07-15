#book module resposible for 'Book' class and book show details method
from product import Product

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price, "Book")
        self.author = author

    def show_details(self):
        _details = super().show_details()
        return f"{_details}, author: {self.author}"