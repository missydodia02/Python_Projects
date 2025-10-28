# FoodProduct class inherits from Product and adds expiry_date feature

from models.product import Product

class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiry_date):
        # Call parent constructor for common attributes
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

    def display_info(self):
        # Override display_info() to also show expiry date
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Expiry Date: {self.expiry_date}")
