#main class 'super'
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def show_details(self):
        return f"name: {self.name}, price: {self.price}, category: {self.category}"