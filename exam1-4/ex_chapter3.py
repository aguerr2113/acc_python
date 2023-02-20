from question import Question

question_prompts = [
    "1.A ___ structure can execute a set of statements only under certain circumstances.\n(a)sequence\n(b)circumstantial\n(c)decision\n(d)Boolean\n",
    

    "2.A ___ structure provides one alternative path of execution.\n(a)sequence\n(b)single alternative decision\n(c)one path alternative\n(d)single execution decision\n",


    "3.	A(n) ___ expression has a value of either True or False.\n(a)binary\n(b)decision\n(c)unconditional\n(d)Boolean\n",


    "4.  The symbols >, <, and == are all ___ operators.\n(a)relational\n(b)logical\n(c)conditional\n(d)ternary\n",

    "5.	A(n) ___ structure tests a condition and then takes one path if the condition is true, or another path if the condition is false.\n(a)if statement\n(b)single alternative decision\n(c)dual alternative decision\n(d)sequence\n",

    "6.	You use a(n) ___ statement to write a single alternative decision structure.\n(a)test-jump\n(b)if\n(c)if-else\n(d)if-call\n",

    "7.	 A ___ is a name that references a value in the computer's memory.\n(a)variable\n(b)register\n(c)RAM slot\n(d)byte\n",


    "8.	and, or, and not are ___ operators.\n(a)relational\n(b)logical\n(c)conditional\n(d)ternary\n",
    

    "9.	A compound Boolean expression created with the ___ operator is true only if both of its subexpressions are true.\n(a)and.\n(b)or.\n(c)dnot.\n(d)both.\n",

    "10. A compound Boolean expression created with the ___ operator is true if either of its subexpressions is true.\n(a)and\n(b)or\n(c)not\n(d)either\n",


    "11.The ___ operator takes a Boolean expression as its operand and reverses its logical value.\n(a)and\n(b)or\n(c)not\n(d)either\n",

    "12.A ___ is a Boolean variable that signals when some condition exists in the program.\n(a)flag\n(b)signal\n(c)sentinel\n(d)siren\n",


    "13. You can write any program using only sequence structures.\n(t)(f)\n",

    "14.A program can be made of only one type of control structure. You cannot combine structures.\n(t)(f)\n",

    "15. A single alternative decision structure tests a condition and then takes one path if the condition is true, or another path if the condition is false.\n(t)(f)\n",

    "16.A decision structure can be nested inside another decision structure.\n(t)(f)\n",

    "17.A compound Boolean expression created with the and operator is true only when both subexpressions are true.\n(t)(f)\n",
   
]
 #-------------------------------------
    # short answer
    # -----------------------------------------------------------------
    # 18  Explain what is meant by the term 'conditionally executed.'
    
    # Is a set of statements that are executed only when a certain condition is true. If the condition is false they will not be executed. Also called a single alternative decision structure.
    #------------------------------------------------------------------
    # 19  You need to test a condition then execute one set of statements if the condition is true. If the condition is false, you need to execute a different set of statements. What structure will you use?"
    
    # A duel alternative decision structure
    # -----------------------------------------------------------------
    # 20 "Briefly describe how the and operator works."
    # The AND operator connects two Boolean expressions into one compound expression. Both subexpressions must be true for the compound expression to be true.
    # -----------------------------------------------------------------
    # 21 "Briefly describe how the or operator works."
    # The OR operator connects two Boolean expressions into one compound expression. One or both subexpressions must be true for the compound expression to be true. It is only necessary for one of the expressions to be true, and it does not matter which.
    # -----------------------------------------------------------------
    # 22 "When determining whether a number is inside a range, which logical operator is it best to use?"
    # The AND operator
    # -----------------------------------------------------------------
    # 23 "What is a flag and how does it work?"
    # A flag is a variable that singnal when some condition exists in the program. When the flag variable is set to False, it indicates the condition does not exist. When tha flag variable is set to True, it means the condition does exist.
# -----------------------------------------------------------------

    # Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z if the variable x is greater than 100.
# if x > 100:
#     y = 20 and z = 40 

# ----------------------------------------------------------------------------------------------------

    # Write an if statement that assigns 0 to the variable b, and assigns 1 to the variable c if the variable a is less than 10.
# if a < 10:
#     b = 0
#     c = 1
#     print(b,c)

# ----------------------------------------------------------------------------------------------------

    # Write an if-else statement that assigns 0 to the variable b if the variable a is less than 10. Otherwise, it should assign 99 to the variable b.
# if a < 10:
#     b = 0
# else:
#     b = 99 

    # 

# ----------------------------------------------------------------------------------------------------

    # The following code contains several nested if-else statements. Unfortunately, it was written without proper alignment and indentation. Rewrite the code and use the proper conventions of alignment and indentation.

    # if score >= A_score:
    #  print('Your grade is A.')
    #  else:
    #  if score >= B_score:
    #  print('Your grade is B.')
    #  else:
    #  if score >= C_score:
    #  print('Your grade is C.')
    #  else:
    #  if score >= D_score:
    #  print('Your grade is D.')
    #  else:
    #  print('Your grade is F.')
    
    
# if score >= A_score:
#     print('Your grade is A.')
# else:
#     if score >= B_score:
#         print('Your grade is B.')
#     else:
#         if score >= C_score:
#             print('Your grade is C.')
#         else:
#             if score >= D_score:
#                 print('Your grade is D.')
#             else:
#                 print('Your grade is F.')
# ----------------------------------------------------------------------------------------------------

    # Write nested decision structures that perform the following: If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2.
# amount1 = int(input('pick number greater or less than 10'))
# amount2 = int(input('pick number greater or less than 100'))

# if amount1 >  10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     elif amount2 > amount1:
#         print(amount2)
# else:
#     print('invalid') 
#     # 
#------------------------------------------------------------------------------------------------
    # Write an if-else statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56. If the speed variable’s value is outside this range, display 'Speed is abnormal'.
    # 
# if speed > 24 or speed < 56:
#     print('speed is normal')
# else:
#     print('speed is abnormal')

# ----------------------------------------------------------------------------------------------------

# Write an if-else statement that determines whether the points variable is outside the range of 9 to 51. If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it should display “Valid points.”

# if points < 9 or points > 51:
#     print('invalid points')
# else:
#     print('valid points')


# ----------------------------------------------------------------------------------------------------
    # Write an if statement that uses the turtle graphics library to determine whether the turtle’s heading is in the range of 0 degrees to 45 degrees (including 0 and 45 in the range). If so, raise the turtle’s pen.


# ----------------------------------------------------------------------------------------------------

    # Write an if statement that uses the turtle graphics library to determine whether the turtle’s pen color is red or blue. If so, set the pen size to 5 pixels.
    # 

# ----------------------------------------------------------------------------------------------------

    # Write an if statement that uses the turtle graphics library to determine whether the turtle is inside of a rectangle. The rectangle’s upper-left corner is at (100, 100) and its lower-right corner is at (200, 200). If the turtle is inside the rectangle, hide the turtle.
    # 
    # 
    # 
    # 

# ----------------------------------------------------------------------------------------------------





questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "c"),
    Question(question_prompts[11], "a"),
    Question(question_prompts[12], "f"),
    Question(question_prompts[13], "f"),
    Question(question_prompts[14], "f"),
    Question(question_prompts[15], "t"),
    Question(question_prompts[16], "t")

]

def run_test(questions):
    score = 0
    for question  in questions:
        answer = input(question.prompt)
        if answer  == question.answer:
            score += 1
            print('Correct')
        elif answer != question.answer:
            print(f"incorrect the correct answer was {question.answer}")
    print(f"You got {score}/{len(questions)} correct")

run_test(questions)