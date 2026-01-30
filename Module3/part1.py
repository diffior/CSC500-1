# Part 1: Restaurant Meal Calculator
# Author: Christian Campbell
# Course: CSC500 Module 3
# Date: 2/30/26

def calculate_meal_total():
    """
    Calculates the total cost of a meal with tip and sales tax.
    Prompts user for food charge, then computes and displays:
    - Food charge
    - Tip amount (18%)
    - Sales tax (7%)
    - Total cost
    """
    
    food_charge = float(input("Enter the charge for the food: $"))
 
    tip_rate = 0.18
    tip_amount = food_charge * tip_rate
    
    tax_rate = 0.07
    tax_amount = food_charge * tax_rate
    
    total = food_charge + tip_amount + tax_amount
    
    # Display results
    print("\n--- Meal Cost Breakdown ---")
    print(f"Food Charge:  ${food_charge:,.2f}")
    print(f"Tip (18%):    ${tip_amount:,.2f}")
    print(f"Sales Tax (7%): ${tax_amount:,.2f}")
    print(f"{'─' * 30}")
    print(f"Total:        ${total:,.2f}")


# Run the program
if __name__ == "__main__":
    calculate_meal_total()