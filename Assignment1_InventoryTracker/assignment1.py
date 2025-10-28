# Simple console-based inventory management project
# You can list, add, update, delete products
# You can also check for low-stock items and apply discounts

# Product list (initial data)
products = [
    {"name": "Milk", "stock": 10, "price": 40, "location": "shelf-1", "tags": {"grocery"}},
    {"name": "Buiscuit", "stock": 9, "price": 30, "location": "shelf-2", "tags": {"clearance"}},
    {"name": "Bread", "stock": 3, "price": 30, "location": "shelf-2", "tags": {"grocery", "clearance"}}   
]

# Constant – defines the low stock limit
LOW_STOCK = 5


# Function 1: List all products
def list_products():
    # Prints all products in a clean, readable format
    for p in products:
        print(f"{p['name']} | Stock: {p['stock']} | Price: {p['price']} | Location: {p['location']} | Tags: {p['tags']}")


# Function 2: Display low-stock warnings
def low_stock_warning():
    # Prints only the products whose stock is below the LOW_STOCK limit
    print("\nLow Stock Items:")
    for p in products:
        if p['stock'] < LOW_STOCK:
            print(f"{p['name']} (Stock: {p['stock']})")


# Function 3: Add a new product
def add_product():
    # Takes input from the user and adds a new product to the list
    name = input("Enter product name: ")
    stock = int(input("Enter stock: "))
    price = float(input("Enter price: "))
    location = input("Enter location: ")
    tags = set(input("Enter tags (comma separated): ").split(","))
    products.append({"name": name, "stock": stock, "price": price, "location": location, "tags": tags})
    print("Product added successfully!!")


# Function 4: Update the stock of an existing product
def update_stock():
    name = input("Enter product name to update: ")
    for p in products:
        if p["name"].lower() == name.lower():
            p["stock"] = int(input("Enter new stock: "))
            print("Stock updated successfully!")
            return
    print("Product not found!")


# Function 5: Delete a product
def delete_product():
    name = input("Enter product name to delete: ")
    for p in products:
        if p["name"].lower() == name.lower():
            products.remove(p)
            print("Product deleted!")
            return
        else:
            print("Product not found!")
            
# Function 6: Calculate the total inventory value
def total_value():
    # Formula: total = sum of (stock * price) for all products
    total = sum(p["stock"] * p["price"] for p in products)
    print(f"Total Inventory Value: ₹{total}")


# Function 7: Apply discounts on clearance items
def apply_discount():
    # Applies a 50% discount on items with the "clearance" tag
    print("\nDiscounted Clearance Items:")
    for p in products:
        if "clearance" in p["tags"]:
            new_price = p["price"] * 0.5
            print(f"{p['name']} | Old Price: ₹{p['price']} | New Price: ₹{new_price}")


# Function 8: Main menu
def main():
    while True:
        # Displays the user menu for performing operations
        print("\n1. List Products\n2. Low Stock\n3. Add Product\n4. Update Stock\n5. Delete Product\n6. Total Value\n7. Show discount item and valuew\n8. Exit")
        choice = input("Enter choice: ")

        # Calls the respective function based on the user's choice
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


# Entry point of the program
if __name__ == "__main__":
    main()
