# Write a 1-2 Line comment at the beginning of your program
# in this program itll ask use the price of individual items,calculate the total cost of the items,and calculate the average cost of the items
hamburger = float(input('What is the cost of a hamburger?'))
fries = float(input('What is the cost of fries?'))
shake = float(input('What is the cost of a shake?'))

# total_Cost & avg_cost is being calculated and rounded to 2 decimals

total_Cost = round((hamburger + fries + shake), 2)
avg_Cost = round(((total_Cost)/3),2)

# total & average are being displayed
print (f"${total_Cost}")
print(f"${avg_Cost}")

# 2-1 When you are adding the three prices for total cost then no need to add them again for average calculations. Use

# average = total_cost/3

# Keep it simple.