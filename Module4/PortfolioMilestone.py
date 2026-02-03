# Part 2: Multiplication and Division of Two Numbers
# Author: Christian Campbell
# Course: CSC500 Module 4
# Date: 2/2/26

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")


if __name__ == "__main__":
    items = []

    for i in range(1, 3):
        print(f"\nItem {i}")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name: ")
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))
        items.append(item)

    print("\nTOTAL COST")
    total_cost = 0
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    print(f"Total: ${total_cost}")
