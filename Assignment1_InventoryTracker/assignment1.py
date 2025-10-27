# ---------------- Inventory Tracker Assignment ----------------
# Ye ek simple console-based inventory management system hai
# Jisme hum products ko list, add, update, delete kar sakte hain
# Saath hi low stock aur discount items bhi check karte hain

# Product list (initial data)
products = [
    {"name": "Milk", "stock": 10, "price": 40, "location": "shelf-1", "tags": {"grocery"}},
    {"name": "Bread", "stock": 3, "price": 30, "location": "shelf-2", "tags": {"grocery", "clearance"}}
]

# Constant - low stock limit
LOW_STOCK = 5

# ---------------------------------------------
# Function 1: List all products
# ---------------------------------------------
def list_products():
    # Har product ko ek readable format me print karta hai
    for p in products:
        print(f"{p['name']} | Stock: {p['stock']} | Price: {p['price']} | Location: {p['location']} | Tags: {p['tags']}")

# ---------------------------------------------
# Function 2: Low Stock Warning
# ---------------------------------------------
def low_stock_warning():
    # Sirf un items ko print karta hai jinka stock LOW_STOCK limit se kam hai
    print("\nLow Stock Items:")
    for p in products:
        if p['stock'] < LOW_STOCK:
            print(f"{p['name']} (Stock: {p['stock']})")

# ---------------------------------------------
# Function 3: Add a new product
# ---------------------------------------------
def add_product():
    # User se product details leke products list me add karta hai
    name = input("Enter product name: ")
    stock = int(input("Enter stock: "))
    price = float(input("Enter price: "))
    location = input("Enter location: ")
    tags = set(input("Enter tags (comma separated): ").split(","))
    products.append({"name": name, "stock": stock, "price": price, "location": location, "tags": tags})
    print("Product added successfully!")

# ---------------------------------------------
# Function 4: Update stock of an existing product
# ---------------------------------------------
def update_stock():
    name = input("Enter product name to update: ")
    for p in products:
        if p["name"].lower() == name.lower():
            p["stock"] = int(input("Enter new stock: "))
            print("Stock updated successfully!")
            return
    print("Product not found!")

# ---------------------------------------------
# Function 5: Delete a product
# ---------------------------------------------
def delete_product():
    name = input("Enter product name to delete: ")
    for p in products:
        if p["name"].lower() == name.lower():
            products.remove(p)
            print("Product deleted!")
            return
    print("Product not found!")

# ---------------------------------------------
# Function 6: Calculate total inventory value
# ---------------------------------------------
def total_value():
    # Formula: total = sum of (stock * price) for all products
    total = sum(p["stock"] * p["price"] for p in products)
    print(f"Total Inventory Value: ₹{total}")

# ---------------------------------------------
# Function 7: Apply discount to clearance items
# ---------------------------------------------
def apply_discount():
    # Sirf un items par 50% discount lagata hai jinme tag me 'clearance' hai
    print("\nDiscounted Clearance Items:")
    for p in products:
        if "clearance" in p["tags"]:
            new_price = p["price"] * 0.5
            print(f"{p['name']} | Old Price: ₹{p['price']} | New Price: ₹{new_price}")

# ---------------------------------------------
# Function 8: Main menu loop
# ---------------------------------------------
def main():
    while True:
        # User menu display karta hai
        print("\n1. List Products\n2. Low Stock\n3. Add Product\n4. Update Stock\n5. Delete Product\n6. Total Value\n7. Apply Discount\n8. Exit")
        choice = input("Enter choice: ")

        # Choice ke according function call hota hai
        if choice == "1":
            list_products()
        elif choice == "2":
            low_stock_warning()
        elif choice == "3":
            add_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            total_value()
        elif choice == "7":
            apply_discount()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Entry point
if __name__ == "__main__":
    main()
