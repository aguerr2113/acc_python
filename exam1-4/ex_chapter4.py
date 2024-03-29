from question import Question

question_prompts = [
    "1A            -controlled loop uses a true/false condition to control the number of times that it repeats.\n(a)Boolean\n(b)condition\n(c)decision\n(d)count\n",
    

    "2.A            -controlled loop repeats a specific number of times.\n(a)Boolean\n(b)condition\n(c)decision\n(d)count\n",

    "3.Each repetition of a loop is known as a(n)           .\n(a)cycle\n(b)revolution\n(c)orbit\n(d)iteration\n",


    "4.The while loop is a            type of loop.\n(a)pretest\n(b)no-test\n(c)prequalified\n(d)post-iterative\n",

    "5.A(n)            loop has no way of ending and repeats until the program is interrupted.\n(a)indeterminate\n(b)interminable\n(c)infinite\n(d)timeless\n",

    "6.The -= operator is an example of a(n)            operator.\n(a)relational\n(b)augmented assignment\n(c)complex assignment\n(d)reverse assignment\n",

    "7.A(n)            variable keeps a running total.\n(a)sentinel\n(b)sum\n(c)total\n(d)accumulator\n",

    "8.A(n)            is a special value that signals when there are no more items from a list of items to be processed. This value cannot be mistaken as an item from the list.\n(a)sentinel\n(b)flag\n(c)signal\n(d)accumulator\n",

    "9.	GIGO stands for            .\n(a)great input, great output.\n(b)garbage in, garbage out.\n(c)GIGahertz Output.\n(d)GIGabyte Operation\n",
    

    "10.The integrity of a program's output is only as good as the integrity of the program's            .\n(a)compiler\n(b)programming language\n(c)input\n(d)debugger\n",

    "11.The input operation that appears just before a validation loop is known as the            .\n(a)prevalidation read\n(b)primordial read\n(c)initialization read\n(d)priming read\n",

    "12.Validation loops are also known as            .\n(a)error traps\n(b)doomsday loops\n(c)error avoidance loops\n(d)defensive loops\n",

    "13. A condition-controlled loop always repeats a specific number of times.\n(t)(f)\n",

    "14.The while loop is a pretest loop.\n(t)(f)\n",

    "15. The following statement subtracts 1 from x: x = x - 1\n(t)(f)\n",

    "16.It is not necessary to initialize accumulator variables.\n(t)(f)\n",

    "17.In a nested loop, the inner loop goes through all of its iterations for every single iteration of the outer loop.\n(t)(f)\n",
    
    "18.To calculate the total number of iterations of a nested loop, add the number of iterations of all the loops.\n(t)(f)\n",
    
    "19.The process of input validation works as follows: when the user of a program enters invalid data, the program should ask the user “Are you sure you meant to enter that?” If the user answers “yes,” the program should accept the data.\n(t)(f)\n",
]

# -----------------------------------------------------------------------------------------------------------------
# short answer
# -----------------------------------------------------------------------------------------------------------------
# question What is a condition-controlled loop?
# -----------------------------------------------------------------------------------------------------------------
# answer 
# A loop that uses a true/false condition to control the number of times that it repeats
# 
# 
# -----------------------------------------------------------------------------------------------------------------
# question What is a count-controlled loop?
# -----------------------------------------------------------------------------------------------------------------
# answer
# A loop that repeats a specific number of times
# 
# 
# 
# -----------------------------------------------------------------------------------------------------------------
# question What is an infinite loop? Write the code for an infinite loop.
# -----------------------------------------------------------------------------------------------------------------
# answer
# An infinite loop in Python is a continuous repetition of the conditional loop until some external factors like insufficient CPU memory, error in the code, etc. occur
# count = 10
# while count > 1:
#     print('Hello World')


# ------------------------------------------------------------------------------------------------------------------
# question Why is it critical that accumulator variables are properly initialized?
# ------------------------------------------------------------------------------------------------------------------
# answer
# A counter is used to control or keep track of the number of times a loop iterates. In a loop, the counter is usually incremented or decremented. if the counter variable is not properly initialized, it will not hold the correct number.

# -----------------------------------------------------------------------------------------------------------------
# 
# -----------------------------------------------------------------------------------------------------------------
# question What is the advantage of using a sentinel?
# -----------------------------------------------------------------------------------------------------------------
# answer
# The advantage of using a sentinel is that the program knows that when it has reached the sentinel, it can stop the loop.
# -----------------------------------------------------------------------------------------------------------------
# 
# -----------------------------------------------------------------------------------------------------------------
# question Why must the value chosen for use as a sentinel be carefully selected?
# -----------------------------------------------------------------------------------------------------------------
# answer
# It must be distinctive so that the program will not recognize the value as a "regular" value which could cause errors.

# -----------------------------------------------------------------------------------------------------------------
# question What does the phrase “garbage in, garbage out” mean?
# -----------------------------------------------------------------------------------------------------------------
#answer
#  It means that the computer cannot tell good data from bad data. So, if you put in bad data, you will get bad output.

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# question Give a general description of the input validation process.
# -----------------------------------------------------------------------------------------------------------------
# answer
# When the input entered is not valid, the program discards it and the user is prompted for the correct input.
# 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# algos
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# __________________________________________________________________________________________________________________
# Write a while loop that lets the user enter a number. The number should be multiplied by 10, and the result assigned to a variable named product. The loop should iterate as long as product is less than 100.
# product = 0
# while product < 100:
#     num = int(input('enter a number:'))
#     product = num * 10

# __________________________________________________________________________________________________________________

# __________________________________________________________________________________________________________________
# Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise it should terminate.
# while True:
#     num1 = int(input('enter number:'))
#     num2 = int(input('enter number:'))
#     total = num1 + num2
#     print(total)
#     command = input('do you wish to do this again?y/n: ')
#     if command != "y":
#         break


# __________________________________________________________________________________________________________________

# __________________________________________________________________________________________________________________
# Write a for loop that displays the following set of numbers:
# __________________________________________________________________________________________________________________
#  0, 10, 20, 30, 40, 50 . . . 1000

# for num in range(0,10001,10):
#     print(num,',',end = "")
# __________________________________________________________________________________________________________________

# __________________________________________________________________________________________________________________
# Write a loop that asks the user to enter a number. The loop should iterate 10 times and keep a running total of the numbers entered.

# total = 0
# for num in range(10):
#     num = int(input("Enter a number:"))
#     total += num
#     print(total)
# __________________________________________________________________________________________________________________

# __________________________________________________________________________________________________________________
# Write a loop that calculates the total of the following series of numbers:


# __________________________________________________________________________________________________________________
 
 
 
# __________________________________________________________________________________________________________________
# Rewrite the following statements using augmented assignment operators.

# x = x + 1
# x+= 1

# x = x * 2
# x *= 2

# x = x / 10
# x /= 10

# x = x − 100
# x -= 100
# __________________________________________________________________________________________________________________
# Write a set of nested loops that display 10 rows of # characters. There should be 15 # characters in each row.
# for row in range (10):
#     for col in range(15):
#         print('#',end = "")
#     print()

# __________________________________________________________________________________________________________________
# Write code that prompts the user to enter a positive nonzero number and validates the input.

# __________________________________________________________________________________________________________________
# Write code that prompts the user to enter a number in the range of 1 through 100 and validates the input.















questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "c"),
    Question(question_prompts[10], "d"),
    Question(question_prompts[11], "a"),
    Question(question_prompts[12], "f"),
    Question(question_prompts[13], "t"),
    Question(question_prompts[14], "t"),
    Question(question_prompts[15], "f"),
    Question(question_prompts[16], "t"),
    Question(question_prompts[17], "f"),
    Question(question_prompts[18], "f")

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