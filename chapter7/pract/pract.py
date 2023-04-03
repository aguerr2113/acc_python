import random

# initialize an empty list with 7 zeros
lottery_num = [0] * 7

# generate 7 random numbers and assign each to a list element
for i in range(7):
    rand_num = random.randint(0, 9)
    lottery_num[i] = rand_num

print(lottery_num)

# display the contents of the list using a loop
print("Lottery number:")
for num in lottery_num:
    print(num, end="")
