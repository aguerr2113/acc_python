from question import Question

question_prompts = [
    "1.	A group of statements that exist within a program for the purpose of performing a specific task is a(n)\n(a)    block\n(b)	parameter\n(c)	function\n(d)	expression:\n",
    
    "2.	A design technique that helps to reduce the duplication of code within a program and is a benefit of using functions is\n(a)	code reuse\n(b)	divide and conquer\n(c)	debugging\n(d)	facilitation of teamwork:\n",
    
    "3.	The first line of a function definition is known as the     .\n(a)body\n(b)introductione\n(c)initialization\n(d)header\n",

    "4. You          a function to execute it.:\n(a)define\n(b)call\n(c)import\n(d)export\n",

    "5.	A design technique that programmers use to break down an algorithm into functions is known as       .\n(a)top-down design\n(b)code simplification\n(c)code refactoring\n(d)hierarchical subtasking\n",
    
    "6. A        is a diagram that gives a visual representation of the relationships between functions in a program.\n(a)flowchart\n(b)function relationship chart\n(c)symbol chart\n(d)hierarchy chart\n",

    "7. The                 keyword is ignored by the Python interpreter and can be used as a placeholder for code that will be written later.\n(a)placeholder\n(b)pass\n(c)pause\n(d)skip\n",

    
    "8. A            is a variable that is created inside a function.\n(a)global variable\n(b)local variable\n(c)hidden variable\n(d)none of the above; you cannot create a variable inside a function\n",

    
    "9.  A(n)            is the part of a program in which a variable may be accessed.\n(a)declaration space\n(b)area of visibility\n(c)scope\n(d)mode\n",
    
    "10. A(n)            is a piece of data that is sent into a function.\n(a)argument\n(b)parameter\n(c)header\n(d)packet\n",

    # ________---_-____---_--_-__--_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---_-_-_-_-_---_-_-_-_-_-_-_--
    # 11 is next i already did 10
    
    "11. A byte is made up of eight\n(a)CPUs\n(b)instructions\n(c)variables\n(d)bits\n",

    
    "12.In the            numbering system, all numeric values are written as sequences of 0s and 1s.\n(a)hexadecimal\n(b)binary\n(c)octal\n(d)decimal\n",


    "13. A bit that is turned off represents the following value:\n(a)1\n(b)-1\n(c)0\n(d)'no'n",


    "14. A set of 128 numeric codes that represent the English letters, various punctuation marks, and other charac\n(a)binary numbering\n(b)ASCII\n(c)Unicode\n(d)ENIAC\n",

    
    "15. An extensive encoding scheme that can represent characters for many languages in the world is .\n(a)binary numbering\n(b)ASCII\n(c)Unicode\n(d)ENIAC\n",
    
    "16. Negative numbers are encoded using the            technique.\n(a)two's complement\n(b)floating point\n(c)ASCII\n(d)Unicode\n",

    "17. Real numbers are encoded using the            technique.\n(a)two's complement\n(b)floating point\n(c)ASCII\n(d)Unicode\n",

    "18. The tiny dots of color that digital images are composed of are called.\n(a)bits\n(b)bytes\n(c)color packets\n(d)pixels\n",
    
    "19.  If you were to look at a machine language program, you would see           .\n(a)Python code\n(b)a stream of binary numbers\n(c)English words\n(d)circuits\n",
    
    "20. In the            part of the fetch-decode-execute cycle, the CPU determines which operation it should perform.\n(a)fetch\n(b)decode\n(c)execute\n(d)deconstructy\n",

    "21. Computers can only execute programs that are written in           .\n(a)Java\n(b)assembly language\n(c)machine language\n(d)Python\n",

    "22. The            translates an assembly language program to a machine language program.\n(a)assembler\n(b)compiler\n(c)translator\n(d)interpreter\n",
    
    "23.The words that make up a high-level programming language are called           .\n(a)binary instructions\n(b)mnemonics\n(c)commands\n(d)keywords\n",

    "24. The rules that must be followed when writing a program are called           .\n(a)syntax\n(b)punctuation\n(c)keywords\n(d)operators\n",

    "25.  A(n)            program translates a high-level language program into a separate machine language program.\n(a)assembler\n(b)compiler\n(c)translator\n(d)utility\n",

    "26. Today, CPUs are huge devices made of electrical and mechanical components such as vacuum tubes and switches.\n(t)(f)\n",

    "27. Main memory is also known as RAM.(t)(f)\n",

    "28. Any piece of data that is stored in a computer's memory must be stored as a binary number.(t)(f)\n",

    "29. Images, like the ones created with your digital camera, cannot be stored as binary numbers.(t)(f)\n",

    "30. Machine language is the only language that a CPU understands.(t)(f)\n",

    "31. Assembly language is considered a high-level language.(t)(f)\n",

    "32. An interpreter is a program that both translates and executes the instructions in a high-level language program.(t)(f)\n",

    "33. A syntax error does not prevent a program from being compiled and executed.(t)(f)\n",

    "34. Windows, Linux, Android, iOS, and macOS are all examples of application software.(t)(f)\n",

    "35. Word processing programs, spreadsheet programs, email programs, web browsers, and games are all examples of utility programs.(t)(f)\n",
    # ----------------------------------------------
    # short answer
    # ----------------------------------------------
    "36.why is the cpu the most important component in a computer?\n",
    # Because the CPU is responsible for managing all the other components: including memory, storage, input and output devices. 

    "37.What number does a bit that is turned on represent?\nWhat number does a bit that is turned off represent?\n",
    # a bit turned on represents one,off represents 0

    "38.What would you call a device that works with binary data?\n",
    # Digital Device


    "39.What are the words that make up a high-level programming language called?\n",
    # Keywords are the words that make up a high-level programming language. 

    "40.What are the short words that are used in assembly language called?\n",
    # mnenomics

    "41.What is the difference between a compiler and an interpreter?\n",
    
    # An interpreter produces a result from a program, while a compiler produces a program written in assembly language.

    "42.What type of software controls the internal operations of the computer's hardware\n",
    # system software such as windows linux mac os

]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "d"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "c"),
    Question(question_prompts[13], "b"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "b"),
    Question(question_prompts[17], "d"),
    Question(question_prompts[18], "b"),
    Question(question_prompts[19], "b"),
    Question(question_prompts[20], "c"),
    Question(question_prompts[21], "a"),
    Question(question_prompts[22], "d"),
    Question(question_prompts[23], "a"),
    Question(question_prompts[24], "b"),
    Question(question_prompts[25], "f"),
    Question(question_prompts[26], "t"),
    Question(question_prompts[27], "t"),
    Question(question_prompts[28], "f"),
    Question(question_prompts[29], "t"),
    Question(question_prompts[30], "f"),
    Question(question_prompts[31], "t"),
    Question(question_prompts[32], "f"),
    Question(question_prompts[33], "f"),
    Question(question_prompts[34], "f"),
    Question(question_prompts[35], "Because the CPU is responsible for managing all the other components: including memory, storage, input and output devices."),
    Question(question_prompts[36], "a bit turned on represents one,off represents 0"),
    Question(question_prompts[37], "Digital Device"),
    Question(question_prompts[38], "Keywords are the words that make up a high-level programming language."),
    Question(question_prompts[39], "mnenomics"),
    Question(question_prompts[40], "An interpreter produces a result from a program, while a compiler produces a program written in assembly language."),
    Question(question_prompts[41], "system software such as windows linux mac os"),


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