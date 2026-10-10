cart = []


def add_item():

    item = input("Enter item name: ")
    price = float(input("Enter item price: "))

    cart.append({"item": item, "price": price})

    print("Item added successfully")


def remove_item():

    item_name = input("Enter item to remove: ")

    for item in cart:

        if item["item"] == item_name:
            cart.remove(item)
            print("Item removed")
            return

    print("Item not found")


def view_cart():

    if len(cart) == 0:
        print("Cart is empty")
        return

    print("\nShopping Cart:")

    for item in cart:
        print(item["item"], "-", item["price"])


def calculate_total():

    total = 0

    for item in cart:
        total += item["price"]

    return total


def checkout():

    total = calculate_total()

    print("\nCheckout")
    print("Total Amount =", total)
    print("Thank you for shopping!")


while True:

    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item()

    elif choice == 2:
        remove_item()

    elif choice == 3:
        view_cart()

    elif choice == 4:
        print("Total =", calculate_total())

    elif choice == 5:
        checkout()
        break

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
