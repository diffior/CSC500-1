# Part 1: Average Rainfall Calculator
# Author: Christian Campbell
# Course: CSC500 Module 5
# Date: 2/13/26

total_months = 0
total_rainfall = 0.0



years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    print(f"\n--- Year {year} ---")
    
    # Inner loop for 12 months
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))

        total_months += 1
        total_rainfall += rainfall

# Calculate average
average_rainfall = total_rainfall / total_months

# Display results
print("\n--- Results ---")
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")