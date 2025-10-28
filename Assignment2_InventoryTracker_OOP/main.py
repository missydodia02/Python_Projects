# Main file that provides the menu and calls service functions

from service.inventory_service import InventoryService

def main():
    inventory = InventoryService()

    while True:
        print("""
        ==== INVENTORY MANAGEMENT MENU ====
        1. Add Product
        2. List All Products
        3. Low Stock Warnings
        4. Update Stock
        5. Delete Product
        6. Total Inventory Value
        7. Apply Discount by Tag (clearance)
        8. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.add_product()
        elif choice == '2':
            inventory.view_products()
        elif choice == '3':
            inventory.low_stock_products()
        elif choice == '4':
            inventory.update_stock()
        elif choice == '5':
            inventory.delete_product()
        elif choice == '6':
            inventory.total_inventory_value()
        elif choice == '7':
            inventory.discount_by_tag()
        elif choice == '8':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
