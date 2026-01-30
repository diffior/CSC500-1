# Part 2: Multiplication and Division of Two Numbers
# Author: Christian Campbell
# Course: CSC500 Module 1
# Date: 1/14/26

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform multiplication
multiplication_result = num1 * num2

# Perform division with error checking
if num2 != 0:
    division_result = num1 / num2
    # Display results
    print(f"\nResults:")
    print(f"{num1} * {num2} = {multiplication_result}")
    print(f"{num1} / {num2} = {division_result}")
else:
    # Handle division by zero error
    print(f"\nResults:")
    print(f"{num1} * {num2} = {multiplication_result}")
    print(f"Error: Cannot divide by zero!")
