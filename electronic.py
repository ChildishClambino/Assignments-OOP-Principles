# electronic module responsible electronic class and electronic show details method
from product import Product

class Electronic(Product):
    def __init__(self, name, price, IMEI):
        super().__init__(name, price, "Electronic")
        self.IMEI = IMEI

    def show_details(self):
        _details = super().show_details()
        return f"{_details}, IMEI: {self.IMEI}"


