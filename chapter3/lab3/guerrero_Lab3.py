# Artemio Guerrero,
# Program Status:Complete
# this program asks user for the number of pachages that the user purchased, and displays the amount of the discount applied, as well as the total amount after discount

user_package = float(input('Enter the number of packages purchased:'))


# this if else logic is used to determine what discount is applied
if user_package >= 10 and user_package<= 49:
    discount = 10
elif user_package >= 50 and user_package<= 99:
    discount = 20
elif user_package >= 100 and user_package<= 149:
    discount = 30
elif user_package >= 150:
    discount = 40
else:
    discount = 0

# this is the price of a single package no disount
package_price = 149
# this gets the total amount of purchase without discount
user_package_price = user_package * package_price
# this gets the total amount with the discount applied
total_amount = user_package_price - (user_package_price * (discount/100))
# this gets the amount of the discount
discount_amount = user_package_price * (discount/100)

print(f'Discount Amount: $ {"%.2f" % discount_amount}')
print(f'Total Amount: $ {"%.2f" % total_amount}')




