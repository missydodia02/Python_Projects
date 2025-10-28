# Handles all product-related operations (add, update, delete, display)

from models.product import Product
from models.food_product import FoodProduct

class InventoryService:
    def __init__(self):
        self.products = []  # List to store all product objects

    def add_product(self, name, price, quantity, is_food=False, expiry_date=None):
        # Check if product with same name already exists
        for p in self.products:
            if p.name.lower() == name.lower():
                print(f"Product '{name}' already exists!")
                return

        # Create either Product or FoodProduct object
        if is_food:
            product = FoodProduct(name, price, quantity, expiry_date)
        else:
            product = Product(name, price, quantity)

        # Add to inventory list
        self.products.append(product)
        print(f"Product '{name}' added successfully!")

    def remove_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                print(f"Product '{name}' removed successfully!")
                return
        print(f" Product '{name}' not found!")

    def update_product(self, name, new_price=None, new_quantity=None):
        for p in self.products:
            if p.name.lower() == name.lower():
                if new_price is not None:
                    p.price = new_price
                if new_quantity is not None:
                    p.quantity = new_quantity
                print(f"Product '{name}' updated successfully!")
                return
        print(f"Product '{name}' not found!")

    def display_all_products(self):
        if not self.products:
            print("Inventory is empty!")
        else:
            print("\nCurrent Inventory:")
            for p in self.products:
                p.display_info()
