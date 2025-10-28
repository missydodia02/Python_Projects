# This file handles inventory operations (add, update, delete, total value, low stock, discount)

from models.product import Product
from models.food_product import FoodProduct

class InventoryService:
    def __init__(self):
        # Store all products
        self.products = []

    def add_product(self):
        choice = input("Enter product type (1 - Normal, 2 - Food): ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        location = input("Enter product location (e.g., shelf-1): ")
        tags = set(input("Enter tags (comma separated, e.g., grocery,clearance): ").split(','))

        if choice == '1':
            product = Product(name, price, quantity, location, tags)
        elif choice == '2':
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            product = FoodProduct(name, price, quantity, location, tags, expiry_date)
        else:
            print("Invalid choice!")
            return

        self.products.append(product)
        print("Product added successfully!\n")

    def view_products(self):
        if not self.products:
            print("No products found!\n")
            return
        print("\n--- Product List ---")
        for product in self.products:
            product.display_info()

    def update_stock(self):
        name = input("Enter product name to update stock: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                product.quantity = int(input("Enter new quantity: "))
                print(" Stock updated successfully!\n")
                return
        print("Product not found!\n")

    def delete_product(self):
        name = input("Enter product name to delete: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(" Product deleted successfully!\n")
                return
        print("Product not found!\n")

    def total_inventory_value(self):
        total = sum(p.value() for p in self.products)
        print(f"\nTotal Inventory Value: {total}\n")

    def low_stock_products(self):
        print("\nLow Stock Products (Quantity < 5):")
        found = False
        for p in self.products:
            if p.quantity < 5:
                p.display_info()
                found = True
        if not found:
            print("All products are sufficiently stocked!\n")

    def discount_by_tag(self):
        print("\nDiscounted Products (Tag = clearance, 50% off):")
        for p in self.products:
            if "clearance" in p.tags:
                discounted_price = p.price * 0.5
                print(f"{p.name} | Original: {p.price} | Discounted: {discounted_price}")
