# Online shopping cart
# Author: Christian Campbell
# Course: CSC500 Module 8
# Date: 3/3/2026

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
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
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip().lower()

        if choice == 'q':
            break
        elif choice == 'a':
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ")
            desc = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            qty = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, price, qty, desc))
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            qty = int(input("Enter the new quantity: "))
            cart.modify_item(ItemToPurchase(name, item_quantity=qty))
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            print("Invalid option. Please try again.")


def main():
    print("Enter customer's name:")
    name = input()
    print("Enter today's date:")
    date = input()
    print(f"\nCustomer name: {name}")
    print(f"Today's date: {date}")

    cart = ShoppingCart(name, date)
    print_menu(cart)


if __name__ == "__main__":
    main()