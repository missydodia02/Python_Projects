# FoodProduct class inherits Product and adds expiry_date feature

from models.product import Product

class FoodProduct(Product):
    def __init__(self, name, price, quantity, location, tags, expiry_date):
        # Initialize parent Product fields using super()
        super().__init__(name, price, quantity, location, tags)
        self.expiry_date = expiry_date

    def display_info(self):
        # Override method to also show expiry date
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, "
              f"Location: {self.location}, Tags: {self.tags}, Expiry Date: {self.expiry_date}")
