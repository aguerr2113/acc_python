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