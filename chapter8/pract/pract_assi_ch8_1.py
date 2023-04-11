# Practice Assignment Ch. 8-1
# Write a program that does the following:
# 1. Accepts input of your first, last, and middle names into three separate strings
# 2. Concatenates them together to form a string called full_name
# 3. Counts the number of “a” or “A” letters
# 4. Counts the number of “e” or “E” letters
# 5. Counts the number of “s” or “S” letters
# 6. Displays each of the three counts
# Turn in your program to the practice assignment link in course content.

first = input("First name:")
last = input('Last name:')
middle = input('middle name:')

full_name = first +" "+ middle +" "+ last
cap_full_name = full_name.upper()
count1 = cap_full_name.count('A')
count2 = cap_full_name.count('E')
count3 = cap_full_name.count('S')
print(f"Full Name: {full_name}")
print(f"the letter 'a' or 'A' appears {count1}")
print(f"the letter 'e' or 'E' appears {count2}")
print(f"the letter 's' or 'E' appears {count3}")