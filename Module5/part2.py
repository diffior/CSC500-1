# Part 2: Book Club Points Awarder
# Author: Christian Campbell
# Course: CSC500 Module 5
# Date: 2/13/26

# Get number of books from operator
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine points based on criteria
if books_purchased >= 8:
    points = 60
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 2:
    points = 5
else:
    points = 0

# Display the points
print(f"Points awarded: {points}")