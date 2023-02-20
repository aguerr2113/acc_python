# Artemio Guerrero,
# complete,
# program asks the user to enter the amount that he or she has budgeted for a month.

# Uses a while loop,so the user is prompted to enter each of his or her expenses for the
# month and keep a running total. 
# When the loop finishes, the program  displays the amount
# that the user is over or under budget

# Enter amount budgeted for the month: 500
# Enter an amount spent(0 to quit): 50
# Enter an amount spent(0 to quit): 75
# Enter an amount spent(0 to quit): 800
# Enter an amount spent(0 to quit): 23.95
# Enter an amount spent(0 to quit): 0
# Budgeted: $ 500.00
# Spent: $ 948.95
# You are $ 448.95 over budget. PLAN BETTER NEXT TIME!



# asks the user to enter the amount that he or she has budgeted for a month.
budget =float(input('Enter amount budgeted for the month:'))
# total spent will start at zero becouse it will be a total acumlator
total_spent = 0


# user is prompted to enter each of his or her expenses for the
# month and keep a running total
while True:
    spent = float(input("Enter an amount spent(0 to quit): "))

    # here we use the accumulate to add the results of the loop
    total_spent += spent
    
    if spent == 0:
        
        break
over_under_total = budget-total_spent

print('Budgeted: $',"%.2f"%(budget))
print('Spent: $',"%.2f"%(total_spent))

if total_spent > budget:
    print('You are $',"%.2f"%(-(over_under_total)), 'over budget. PLAN BETTER NEXT TIME!')

# Feedback to Learner
# 2/20/23 8:29 AM
# In 4.1, what if the difference is 0 have message for it too.
elif total_spent == budget:
    print('You are $',"%.2f"%((over_under_total)), 'over budget.Congratulatons on staying within budget!')


else:
    print('You are $',"%.2f"%((over_under_total)), 'under budget.Great Job')

