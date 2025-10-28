import numpy as np
from models.food_product import FoodProduct
from models.product import Product

LOW_STOCK = 5

class InventoryService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if not self.products:
            print("No products available.")
        else:
            for p in self.products:
                p.display_info()

    def low_stock_warning(self):
        print("\nLow Stock Products (below 5):")
        found = False
        for p in self.products:
            if p.quantity < LOW_STOCK:
                p.display_info()
                found = True
        if not found:
            print("No low-stock products.")

    def update_stock(self, name, quantity):
        for p in self.products:
            if p.name == name:
                p.quantity = quantity
                print("Stock updated successfully!")
                return
        print("Product not found.")

    def delete_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print("Product deleted successfully!")
                return
        print("Product not found.")

    def total_value(self):
        total = sum(p.value() for p in self.products)
        print(f"\nTotal value of all products: ₹{total}")

    # def apply_discount_by_tag(self, tag):
    #     print(f"\nApplying discount for tag: {tag}")
    #     for p in self.products:
    #         if hasattr(p, "tags") and tag in p.tags:
    #             old_price = p.price
    #             p.price = p.price * 0.5
    #             print(f"{p.name} discounted from ₹{old_price} to ₹{p.price}")

    
    # NumPy Stats Feature
    
    def show_statistics(self):
        if not self.products:
            print("No products to analyze.")
            return

        prices = np.array([p.price for p in self.products])
        quantities = np.array([p.quantity for p in self.products])
        total_values = np.array([p.value() for p in self.products])

        print("\n--- Inventory Statistics ---")
        print(f"Average Price: ₹{np.mean(prices):.2f}")
        print(f"Most Expensive Item Price: ₹{np.max(prices):.2f}")
        print(f"Total Count of All Items: {np.sum(quantities)}")
        print(f"Total Inventory Value: ₹{np.sum(total_values):.2f}")

        # Clearance tag-based stats
        # clearance_products = [p for p in self.products if hasattr(p, "tags") and "clearance" in p.tags]
        # if clearance_products:
        #     clearance_prices = np.array([p.price for p in clearance_products])
        #     clearance_values = np.array([p.value() for p in clearance_products])
        #     print("\n--- Clearance Items Stats ---")
        #     print(f"Average Price: ₹{np.mean(clearance_prices):.2f}")
        #     print(f"Total Value: ₹{np.sum(clearance_values):.2f}")
        # else:
        #     print("\nNo clearance items available.")
