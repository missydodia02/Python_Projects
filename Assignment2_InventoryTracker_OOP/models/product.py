# Product class – represents a basic product in the inventory

class Product:
    def __init__(self, name, price, quantity):
        # Initialize the product with name, price, and quantity
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        # Display all product details
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def value(self):
        # Calculate total value of this product (price × quantity)
        return self.price * self.quantity
