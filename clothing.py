# clothing modul responsible for the clothing class and clothing show_details method
from product import Product

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price, "Clothing")
        self.size = size

    def show_details(self):
        _details = super().show_details()
        return f"{_details}, Size: {self.size} "