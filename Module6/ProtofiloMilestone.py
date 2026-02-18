class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


# ── Step 4 ─────────────────────────────────────────────────────────────────────

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Adds an ItemToPurchase to cart_items."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Removes an item by name. Prints message if not found."""
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        """
        Modifies description, price, and/or quantity of a matching cart item.
        Only updates fields that differ from their defaults.
        Prints message if item not found.
        """
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Returns total quantity of all items."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Returns total cost of all items."""
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        """Prints a formatted summary of the cart and total cost."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.0f} = ${total:.0f}")
            print()
            print(f"Total: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        """Prints each item's name and description."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# ── Step 5 & 6 ─────────────────────────────────────────────────────────────────

def print_menu(cart):
    """Displays the menu and handles user input until 'q' is chosen."""
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            break

        elif choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            date = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, date))

        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))

        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        else:
            print("Invalid option. Please choose a valid menu item.")


def main():
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()