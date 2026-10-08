import requests


BASE_URL = "http://127.0.0.1:5000"


def show_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View inventory")
    print("2. View one item")
    print("3. Add item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Search Open Food Facts")
    print("7. Import product from Open Food Facts")
    print("8. Exit")


def main():

    while True:

        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":

            response = requests.get(
                f"{BASE_URL}/inventory"
            )

            print(response.json())

        elif choice == "2":

            item_id = input("Enter item ID: ")

            response = requests.get(
                f"{BASE_URL}/inventory/{item_id}"
            )

            print(response.json())

        elif choice == "3":

            name = input("Product name: ")
            barcode = input("Barcode: ")
            category = input("Category: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            data = {
                "name": name,
                "barcode": barcode,
                "category": category,
                "price": price,
                "quantity": quantity
            }

            response = requests.post(
                f"{BASE_URL}/inventory",
                json=data
            )

            print(response.json())

        elif choice == "4":

            item_id = input("Enter item ID: ")
            price = float(input("New price: "))
            quantity = int(input("New quantity: "))

            data = {
                "price": price,
                "quantity": quantity
            }

            response = requests.patch(
                f"{BASE_URL}/inventory/{item_id}",
                json=data
            )

            print(response.json())

        elif choice == "5":

            item_id = input("Enter item ID: ")

            response = requests.delete(
                f"{BASE_URL}/inventory/{item_id}"
            )

            print(response.json())

        elif choice == "6":

            barcode = input("Enter barcode: ")

            response = requests.get(
                f"{BASE_URL}/products/barcode/{barcode}"
            )

            print(response.json())

        elif choice == "7":

            barcode = input("Enter barcode: ")

            response = requests.post(
                f"{BASE_URL}/inventory/import/{barcode}"
            )

            print(response.json())

        elif choice == "8":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()