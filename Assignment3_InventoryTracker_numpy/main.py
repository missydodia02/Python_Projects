from models.product import Product
from models.food_product import FoodProduct
from services.inventory_service import InventoryService

inventory = InventoryService()

while True:
    print("\n===== Inventory Menu =====")
    print("1. List Products")
    print("2. Low Stock Warning")
    print("3. Add Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Total Value")
    print("7. Show Statistics (NumPy)")
    print("8. Exit")

    # print("7. Apply Discount by Tag")
    # print("8. Show Statistics (NumPy)")
    # print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        inventory.list_products()
    elif choice == '2':
        inventory.low_stock_warning()
    elif choice == '3':
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        tags = input("Enter tags (comma separated): ").split(',')
        p = Product(name, price, qty)
        p.tags = [t.strip() for t in tags]
        inventory.add_product(p)
    elif choice == '4':
        name = input("Enter product name: ")
        qty = int(input("Enter new quantity: "))
        inventory.update_stock(name, qty)
    elif choice == '5':
        name = input("Enter product name: ")
        inventory.delete_product(name)
    elif choice == '6':
        inventory.total_value()
    # elif choice == '7':
    #     tag = input("Enter tag to apply discount (e.g., clearance): ")
    #     inventory.apply_discount_by_tag(tag)
    elif choice == '7':
        inventory.show_statistics()
    elif choice == '8':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
