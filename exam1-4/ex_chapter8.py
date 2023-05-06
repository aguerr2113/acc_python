from question import Question

question_prompts = [

    "Review Questionsn\n\nMultiple Choicen\n\n1.	This is the first index in a string.\nA.	-1\nB.	1\nC.	0\nD.	The size of the string minus    one\n\n",

    "2.	This is the last index in a string.\nA.	1\nB.	99\nC.	0\nD.	The size of the string minus one\n\n",

    "3.	This will happen if you try to use an index that is out of range for a string.\nA.	A ValueError exception will occur.\nB.	An IndexError exception     will occur.\nC.	The string will be erased and the program will continue to run.\nD.	Nothing—the invalid index will be ignored.\n\n",

    "4.	This function returns the length of a string.\nA.	length\nB.	size\nC.	len\nD.	lengthof\n\n",

    "5.	This string method returns a copy of the string with all leading whitespace characters removed.\nA.	lstrip\nB.	rstrip\nC.	remove\nD.	    strip_leading\n\n",

    "6.	This string method returns the lowest index in the string where a specified substring is found.\nA.	first_index_of\nB.	locate\nC.	find\nD.	    index_of\n\n",

    "7.	This operator determines whether one string is contained inside another string.\nA.	contains\nB.	is_in\nC.	==\nD.	in\n\n",

    "8.	This string method returns true if a string contains only alphabetic characters and is at least one character in length.\nA.	the isalpha     method\nB.	the alpha method\nC.	the alphabetic method\nD.	the isletters method\n\n",

    "9.	This string method returns true if a string contains only numeric digits and is at least one character in length.\nA.	the digit method\nB.	the     isdigit method\nC.	the numeric method\nD.	the isnumber method\n\n",

    "10.	This string method returns a copy of the string with all leading and trailing whitespace characters removed.\nA.	clean\nB.	strip\nC.	    remove_whitespace\nD.	rstrip\n\n",

    "True or False\n\n1.	Once a string is created, it cannot be changed.(t)(f)\n\n",

    "2.	You can use the for loop to iterate over the individual characters in a string.(t)(f)\n\n",

    "3.	The isupper method converts a string to all uppercase characters.(t)(f)\n\n",

    "4.	The repetition operator (*) works with strings as well as with lists.(t)(f)\n\n",

    "5.	When you call a string's split method, the method divides the string into two substrings.(t)(f)\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "b"),
    #################################
    Question(question_prompts[10], "t"),
    Question(question_prompts[11], "t"),
    Question(question_prompts[12], "f"),
    Question(question_prompts[13], "t"),
    Question(question_prompts[14], "f"),
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
