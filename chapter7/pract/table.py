# Practice Assignment Ch. 7-4

# Write a program that creates a two dimensional list with 4
# rows and 3 columns.

# 1. Write a nested loop to get an integer value from the user
# for each element in the list.

# 2. Write another nested loop to sum and display each
# element in the list.

# 3. Print the total of all elements

# Turn in your program to the practice assignment link in
# course content.
def main():

    row = 4
    column = 3
    table = []
    total = 0
    
    for i in range(row):
        rows = []
        for j in range(column):
            num = int(input("Enter element at row {} and column {}: ".format(i+1, j+1)))
            rows.append(num)
            total += num
        table.append(rows)

 # Loop to sum and display each element in the list
    for i in range(row):
        for j in range(column):
            print(table[i][j], end=" ")
        print()
    
    # Print the total of all elements
    print("Total: ", total)

if __name__ == '__main__':
    main()
