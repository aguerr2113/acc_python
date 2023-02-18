# Artemio Guerrero,
# complete,
# This program should ask the user how many servings they want to make then display the amount of each ingredient needed for the specified number of servings.

# this divides the 4 servings of ingrediants to a single serving

# this is my list og named  constants
og_recipie = 4

tomato_sauce = (2/og_recipie)
tomato_paste = (1/3)/og_recipie
garlic = 2/og_recipie
oregano = 1/og_recipie

# asks user for amount of servings they want to make
serving = float(input('Enter the number of servings of spaghetti sauce you want to make: '))
new_tomato_sauce = tomato_sauce*serving
new_tomato_paste = tomato_paste*serving
new_garlic = garlic*serving
new_oregano = oregano*serving


# f string solution I was just running into an issue with how to round to the second decimal place.
# print(f"To make {serving} servings of spaghetti sauce, you will need:\n{tomato_sauce * serving} cups of tomato sauce\n{tomato_paste * serving} cups of tomato paste\n{garlic * serving} cloves of garlic\n{oregano * serving} tablespoons of oregano")
# gives the user how much of each ingrediant is needed by (*) serving with ingrediant
print(f'To make {serving} servings of spaghetti sauce, you will need:')
print("%.2f" % (new_tomato_sauce),'cups of tomato sauce')
print("%.2f" % (new_tomato_paste),'cups of tomato paste')
print("%.2f" % (new_garlic),'cloves of garlic')
print("%.2f" % (new_oregano),'tablespoons of oregano')