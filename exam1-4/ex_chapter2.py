from question import Question

question_prompts = [
    "1.	A ___ error does not prevent the program from running, but causes it to produce incorrect results.\n(a)	syntax\n(b)	hardware\n(c)	logic\n(d)	fatal\n",
    

    "2.	 A ___ is a single function that the program must perform in order to satisfy the customer.\n(a)task\n(b)software requirement\n(c)prerequisite\n(d)predicate\n",
    

    "3.	A(n) ___ is a set of well-defined logical steps that must be taken to perform a task.\n(a)logarithm\n(b)plan of action\n(c)logic schedule\n(d)algorithm\n",

    "4.  An informal language that has no syntax rules and is not meant to be compiled or executed is called.\n(a)faux code\n(b)pseudocode\n(c)Python\n(d)a flowchart\n",

    "5.	A ___ is a diagram that graphically depicts the steps that take place in a program.\n(a)flowchart\n(b)step chart\n(c)code graph\n(d)program graph\n",

    "6.	A ___ is a sequence of characters.\n(a)char sequence\n(b)scharacter collection\n(c)string\n(d)text block\n",


    "7.	 A ___ is a name that references a value in the computer's memory.\n(a)variable\n(b)register\n(c)RAM slot\n(d)byte\n",


    "8.	A ___ is any hypothetical person using a program and providing input for it.\n(a)designer\n(b)user\n(c)guinea pig\n(d)test subject\n",
    
    "9.	A string literal in Python must be enclosed in \n(a)parentheses.\n(b)single-quotes.\n(c)double-quotes.\n(d)either single-quotes or double-quotes.\n",


    "10.Short notes placed in different parts of a program explaining how those parts of the program work are called\n(a)comments\n(b)reference manuals\n(c)tutorials\n(d)external documentation\n",


    "11.A(n) ___ makes a variable reference a value in the computer's memory.\n(a)variable declaration\n(b)assignment statement\n(c)math expression\n(d)string literal\n",
    

    "12.This symbol marks the beginning of a comment in Python.\n(a)&\n(b)*\n(c)c**\n(d)#\n",


    "13.Which of the following statements will cause an error?\n(a)x = 17\n(b)17 = x\n(c)x = 99999\n(d)x = '17'\n",

    
    "14.In the expression 12 + 7, the values on the right and left of the + symbol are called___.\n(a)operands\n(b)operators\n(c)arguments\n(d)math expressions\n",

    
    
    "15.This operator performs integer division.\n(a)//\n(b)%\n(c)**\n(d)/\n",

    
    "16.This is an operator that raises a number to a power.\n(a)%\n(b)*\n(c)**\n(d)/\n",
    
    "17.This operator performs division, but instead of returning the quotient it returns the remainder.\n(a)%\n(b)*\n(c)**\n(d)/\n",

    "18.Suppose the following statement is in a program: price = 99.0. After this statement executes, the price variable will reference a value of which data type?\n(a)int\n(b)float\n(c)currency\n(d)str\n",

    "19.Which built-in function can be used to read input that has been typed on the keyboard?\n(a)input()\n(b)get_input()\n(c)read_input()\n(d)keyboard()\n",


    "20.Which built-in function can be used to convert an int value to a float?\n(a)int_to_float()\n(b)float()\n(c)convert()\n(d)int()\n",

    "21.	A magic number is ___.\n(a)a number that is mathematically undefined\n(b)an unexplained value that appears in a program's code\n(c)a number that cannot be divided by 1\n(d)a number that causes computers to crash\n",

    "22.A ___ is a name that represents a value that does not change during the program's execution.\n(a)named literal\n(b)named constant\n(c)variable signature\n(d)key term\n",

    "23. Programmers must be careful not to make syntax errors when writing pseudocode programs..(t)(f)\n",

    "24.In a math expression, multiplication and division take place    before addition and subtraction.(t)(f)\n",

    "25. Variable names can have spaces in them.(t)(f)\n",

    "26.In Python, the first character of a variable name cannot be a   number.(t)(f)\n",

    "27.If you print a variable that has not been assigned a value, the number 0 will be displayed.(t)(f)\n",
    # ----------------------------------------------
    # short answer
    # ----------------------------------------------
    "28.What does a professional programmer usually do first to gain an understanding of a problem?\n",
    # They would first need to understand the requirements that are needed for the program.  Requirements include the task or goals which the program has to perform.
    # ----------------------------------------------
    "29.What is pseudocode?\n",
    # Puedo code is an informal description of an algorithm, which doesn't include syntax
    # ----------------------------------------------
    "30.Computer programs typically perform what three steps?\n",
    # input is received
    # some process has to be performed on the out
    # Output
    # ----------------------------------------------
    "31.If a math expression adds a float to an int, what will the data type of the result be?\n",
    # The result would be given as float data.
    # ----------------------------------------------
    "32.What is the difference between floating-point division and integer division?\n",
    # Float division: gives a decimal answer. Integer division: gives the answer in whole numbers ----------------------------------------------
    "33.What is a magic number?\nWhy are magic numbers problematic?\n",
    #  A unique value with unexplained meaning 
    #  it makes code difficult to understand and maintain.
    # ----------------------------------------------
    "34.Assume a program uses the named constant PI to represent the value 3.14159. The program uses the named constant in several statements. What is the advantage of using the named constant instead of the actual value 3.14159 in each statement?\n",
    #The named constant makes the program more self-explanatory ,widespread changes can easily be made to the program,and  it helps to prevent the typographical errors that are common when using magic numbers

]
#35 Write Python code that prompts the user to enter his or her height and assigns the user’s input to a variable named height.
# print("Enter the height in meters:")
# height = input()
# print("You are", height)

#36 Write Python code that prompts the user to enter his or her favorite color and assigns the user’s input to a variable named color.
# color=input('Enter your favorite color')

#37 Write assignment statements that perform the following operations with the variables a, b, and c:

#38 Adds 2 to a and assigns the result to b
# b = a + 2


#39 Multiplies b times 4 and assigns the result to a
# a = b * 4

#40 Divides a by 3.14 and assigns the result to b
# b = a / 3.14

#41 Subtracts 8 from b and assigns the result to a
# a = b - 8

#42 Assume the variables result, w, x, y, and z are all integers, and that w = 5, x = 4, y = 8, and z = 2. What value will be stored in result after each of the following statements execute?

#43 result = x + y 
# 12

#44 result = z * 2
# 4

#45 result = y / x
# 2.0

#46 result = y – z
# 6

#47 result = w // z
# 2

#48 Write a Python statement that assigns the sum of 10 and 14 to the variable total.
# total=10+14

# print(total)

# output:

# 24



#49 Write a Python statement that subtracts the variable down_payment from the variable total and assigns the result to the variable due.
# 
# total =500
# down_payment = 200
# due = total - down_payment
# print(due)


#50 Write a Python statement that multiplies the variable subtotal by 0.15 and assigns the result to the variable total.
#  total = subtotal * 0.15

#51 What would the following display?
#  a = 5
#  b = 2
#  c = 3
#  result = a + b * c
#  print(result)
# 11












questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "d"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "c"),
    Question(question_prompts[16], "a"),
    Question(question_prompts[17], "b"),
    Question(question_prompts[18], "a"),
    Question(question_prompts[19], "b"),
    Question(question_prompts[20], "b"),
    Question(question_prompts[21], "b"),
    Question(question_prompts[22], "f"),
    Question(question_prompts[23], "t"),
    Question(question_prompts[24], "f"),
    Question(question_prompts[25], "t"),
    Question(question_prompts[26], "f"),
    Question(question_prompts[27], "They would first need to understand the requirements that are needed for the program.  Requirements include the task or goals which the program has to perform."),
    Question(question_prompts[28], "Puedo code is an informal description of an algorithm, which doesn't include syntax"),
    Question(question_prompts[29], "input is received,some process has to be performed on the out,Output"),
    Question(question_prompts[30], "The result would be given as float data."),
    Question(question_prompts[31], "Float division: gives a decimal answer. Integer division: gives the answer in whole numbers"),
    Question(question_prompts[32], "A unique value with unexplained meaning ,it makes code difficult to understand and maintain."),
    Question(question_prompts[33], "The named constant makes the program more self-explanatory ,widespread changes can easily be made to the program,and  it helps to prevent the typographical errors that are common when using magic numbers"),

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