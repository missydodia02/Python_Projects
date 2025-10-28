# Main file that displays menu and handles user interaction

from service.inventory_service import InventoryService

inventory = InventoryService()

while True:
    print("\n==== Inventory Menu ====")
    print("1. Add Normal Product")
    print("2. Add Food Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Display All Products")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        inventory.add_product(name, price, quantity)

    elif choice == "2":
        name = input("Enter Food Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
        inventory.add_product(name, price, quantity, is_food=True, expiry_date=expiry)

    elif choice == "3":
        name = input("Enter Product Name to Update: ")
        price = float(input("Enter New Price: "))
        quantity = int(input("Enter New Quantity: "))
        inventory.update_product(name, price, quantity)

    elif choice == "4":
        name = input("Enter Product Name to Delete: ")
        inventory.remove_product(name)

    elif choice == "5":
        inventory.display_all_products()

    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Try again.")
