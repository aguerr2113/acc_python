# Practice Assignment Ch. 7-1
# Turn in your program to the practice assignment link in course
# content.
import random

# 3. Tip: You will need to create/initialize your list before you can
# assign numbers to it.
values = []
# 1. Lottery number generator: Write a program that generates a seven-digit lottery number. The program should have a loop to generate seven random numbers, each in the range 0 through 9 and assign each number to a list element.

for num in range(7):
    lotto_num = random.randint(1,9)

    values.append(lotto_num)


# print(values)

# 2. Write another loop to display the contents of the list.
for num in values:
    print(num,end="")

