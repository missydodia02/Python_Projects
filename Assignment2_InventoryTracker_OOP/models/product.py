# This class defines a generic product with name, price, quantity, location, and tags

class Product:
    def __init__(self, name, price, quantity, location, tags):
        # Initialize product details
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location
        self.tags = tags  # example: {"grocery"} or {"clearance"}

    def display_info(self):
        # Display all product details
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Location: {self.location}, Tags: {self.tags}")

    def value(self):
        # Calculate total stock value (price × quantity)
        return self.price * self.quantity
