# Total Sales
# Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
# Sure, I can help you with that!

# IPO Chart:

# Input:

# Store sales for each day of the week
# Process:

# Use a loop to iterate through each day of the week
# Add each day's sales to a running total
# Output:

# Total sales for the week
# Pseudo Code:

# Initialize a list to store the sales for each day of the week
# Use a loop to ask the user for the sales for each day of the week and store them in the list
# Initialize a variable to keep track of the total sales and set it to zero
# Use a loop to iterate through the sales list
# Add each day's sales to the total sales variable
# Display the total sales for the week

weekdays = 7

value = [] * weekdays
for index in range(len(value)):
    value[index] = float(input(f"please enter sales for day {}"))