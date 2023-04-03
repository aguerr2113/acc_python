from question import Question

question_prompts = [
    "1.	A group of statements that exist within a program for the purpose of performing a specific task is a(n)\n(a)    block\n(b)	parameter\n(c)	function\n(d)	expression:\n\n",
    
    "2.	A design technique that helps to reduce the duplication of code within a program and is a benefit of using functions is\n(a)	code reuse\n(b)	divide and conquer\n(c)	debugging\n(d)	facilitation of teamwork:\n\n",
    
    "3.	The first line of a function definition is known as the     .\n(a)body\n(b)introductione\n(c)initialization\n(d)header\n\n",

    "4. You          a function to execute it.:\n(a)define\n(b)call\n(c)import\n(d)export\n\n",

    "5.	A design technique that programmers use to break down an algorithm into functions is known as       .\n(a)top-down design\n(b)code simplification\n(c)code refactoring\n(d)hierarchical subtasking\n\n",
    
    "6. A        is a diagram that gives a visual representation of the relationships between functions in a program.\n(a)flowchart\n(b)function relationship chart\n(c)symbol chart\n(d)hierarchy chart\n\n",

    "7. The                 keyword is ignored by the Python interpreter and can be used as a placeholder for code that will be written later.\n(a)placeholder\n(b)pass\n(c)pause\n(d)skip\n\n",

    
    "8. A            is a variable that is created inside a function.\n(a)global variable\n(b)local variable\n(c)hidden variable\n(d)none of the above; you cannot create a variable inside a function\n\n",

    
    "9.  A(n)            is the part of a program in which a variable may be accessed.\n(a)declaration space\n(b)area of visibility\n(c)scope\n(d)mode\n\n",
    
    "10. A(n)            is a piece of data that is sent into a function.\n(a)argument\n(b)parameter\n(c)header\n(d)packet\n\n",

    
    "11. A(n) _______ is a special variable that receives a piece of data when a function is called.\n(a)argument\n(b)parameter\n(c)header\n(d)packet\n\n",


    "12A variable that is visible to every function in a program file is a __________.\n(a)local variable\n(b)universal variable\n(c)program-wide variable\n(d)global variable\n\n",



    "13. When possible, you should avoid using _________ variables in a program.\n(a)local\n(b)global\n(c)reference\n(d)parameter\n\n",


    "14.This is a prewritten function that is built into a programming language.\n(a)standard function\n(b)library function\n(c)custom function\n(d)cafeteria function\n\n",

    
    "15. This standard library function returns a random integer within a specified range of values.\n(a)random\n(b)randint\n(c)random_integer\n(d)uniform\n\n",
    

    "16. This standard library function returns a random floating-point number in the range of 0.0 up to 1.0 (but not including 1.0).\n(a)random\n(b)randint\n(c)random_integer\n(d)uniform\n\n",


    "17. This standard library function returns a random floating-point number within a specified range of values.\n(a)random\n(b)randint\n(c)random_integer\n(d)uniform\n\n",

    "18. This statement causes a function to end and sends a value back to the part of the program that called the function.\n(a)end\n(b)send\n(c)exit\n(d)return\n\n",
    
    "19.This is a design tool that describes the input, processing, and output of a function.\n(a)hierarchy chart\n(b)IPO chart\n(c)datagram chart\n(d)data processing chart\n\n",
    

    "20. This type of function returns either True or False.\n(a)Binary\n(b)true_fasle\n(c)Boolean\n(d)logical\n\n",

    "21. This is a math module function.\n(a)derivative\n(b)factor\n(c)sqrt\n(d)differentiate\n\n",



    "True or False\n22. The phrase “divide and conquer” means that all of the programmers on a team should be divided and work in isolation.(t)(f)\n\n",
    
    "23.Functions make it easier for programmers to work in teams.(t)(f)\n\n",

    "24.Function names should be as short as possible.(t)(f)\n\n",

    "25.Calling a function and defining a function mean the same thing.(t)(f)\n\n",

    "26.A flowchart shows the hierarchical relationships between functions in a program.\n(t)(f)\n\n",

    "27.A hierarchy chart does not show the steps that are taken inside a function.(t)(f)\n\n",

    "28. A statement in one function can access a local variable in another function.(t)(f)\n\n",

    "29.In Python, you cannot write functions that accept multiple arguments.(t)(f)\n\n",

    "30. In Python, you can specify which parameter an argument should be passed into a function call.(t)(f)\n\n",

    "31.You cannot have both keyword arguments and non-keyword arguments in a function call.(t)(f)\n\n",

    "32. Some library functions are built into the Python interpreter.(t)(f)\n\n",

    "33. You do not need to have an import statement in a program to use the functions in the random module.(t)(f)\n\n",

    "34.Complex mathematical expressions can sometimes be simplified by breaking out part of the expression and putting it in a function.(t)(f)\n\n",

    "35. A function in Python can return more than one value.(t)(f)\n\n",

    "36. IPO charts provide only brief descriptions of a function's input, processing, and output, but do not show the specific steps taken in a function.(t)(f)\n\n",

]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "d"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "d"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "b"),
    Question(question_prompts[14], "b"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "d"),
    Question(question_prompts[17], "d"),
    Question(question_prompts[18], "b"),
    Question(question_prompts[19], "c"),
    Question(question_prompts[20], "c"),
    Question(question_prompts[21], "f"),
    Question(question_prompts[22], "t"),
    Question(question_prompts[23], "f"),
    Question(question_prompts[24], "f"),
    Question(question_prompts[25], "t"),
    Question(question_prompts[26], "t"),
    Question(question_prompts[27], "f"),
    Question(question_prompts[28], "f"),
    Question(question_prompts[29], "t"),
    Question(question_prompts[30], "f"),
    Question(question_prompts[31], "t"),
    Question(question_prompts[32], "f"),
    Question(question_prompts[33], "t"),
    Question(question_prompts[34], "t"),
    Question(question_prompts[35], "t"),
]







def run_test(questions):
    score = 0
    for question  in questions:
        answer = input(question.prompt)
        if answer  == question.answer:
            score += 1
            print('\n[Correct]\n')
        elif answer != question.answer:
            print(f"\nincorrect the correct answer was {question.answer}\n")
    print(f"\nYou got {score}/{len(questions)} correct\n")

run_test(questions)