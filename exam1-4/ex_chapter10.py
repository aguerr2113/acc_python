from question import Question

question_prompts = [

    "Review Questions\n\nMultiple Choice\n\n1.	The _____ programming practice is centered on creating functions that are separate from the data that they  work on.\na.	modular\nb.	procedural\nc.	functional\nd.	object-oriented\n\n",

    "2.	The _____ programming practice is centered on creating objects.\na.	object-centric\nb.	objective\nc.	procedural\nd.	object-oriented\n\n",

    "3.	A(n) _____ is a component of a class that references data.\na.	method\nb.	instance\nc.	data attribute\nd.	module\n\n",

    "4.	An object is a(n) _____.\na.	blueprint\nb.	cookie cutter\nc.	variable\nd.	instance\n\n",

    "5.	By doing this, you can hide a class's attribute from code outside the class.\na.	avoid using the self parameter to create the attribute\nb.	    begin the attribute's name with two underscores\nc.	begin the name of the attribute with private_ _\nd.	begin the name of the attribute with the @  symbol\n\n",

    "6.	A(n) _____ method gets the value of a data attribute but does not change it.\na.	retriever\nb.	constructor\nc.	mutator\nd.	accessor\n\n",

    "7.	A(n) _____ method stores a value in a data attribute or changes its value in some other way.\na.	modifier\nb.	constructor\nc.	mutator\nd.	    accessor\n\n",

    "8.	The _____ method is automatically called when an object is created.\na.	_ _init_ _\nb.	init\nc.	_ _str_ _\nd.	_ _object_ _\n\n",

    "9.	If a class has a method named _ _str_ _, which of these is a way to call the method?\na.	you call it like any other method: object._ _str_ _()   \nb.	by passing an instance of the class to the built in str function\nc.	the method is automatically called when the object is created\nd.	by  passing an instance of the class to the built-in state function\n\n",

    "10.	A set of standard diagrams for graphically depicting object-oriented systems is provided by _____.\na.	the Unified Modeling Language\nb.	    flowcharts\nc.	pseudocode\nd.	the Object Hierarchy System\n\n",

    "11.	In one approach to identifying the classes in a problem, the programmer identifies the _____ in a description of the problem domain.\na.	    verbs\nb.	adjectives\nc.	adverbs\nd.	nouns\n\n",

    "12.	In one approach to identifying a class's data attributes and methods, the programmer identifies the class's _____.\na.	responsibilities\nb.	    name\nc.	synonyms\nd.	nouns\n\n",

    "True or False\n\n1.	The practice of procedural programming is centered on the creation of objects.(t)(f)\n\n",

    "2.	Object reusability has been a factor in the increased use of object-oriented programming\.(t)(f)\n\n",

    "3.	It is a common practice in object-oriented programming to make all of a class's data attributes accessible to statements outside the class.(t)(f)   \n\n",

    "4.	A class method does not have to have a self parameter.(t)(f)\n\n",

    "5.	Starting an attribute name with two underscores will hide the attribute from code outside the class.(t)(f)\n\n",

    "6.	You cannot directly call the _ _str_ _ method.(t)(f)\n\n",

    "7.	One way to find the classes needed for an object-oriented program is to identify all of the verbs in a description of the problem domain.(t)(f) \n\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"d"),
    Question(question_prompts[2],"c"),
    Question(question_prompts[3],"d"),
    Question(question_prompts[4],"b"),
    Question(question_prompts[5],"d"),
    Question(question_prompts[6],"c"),
    Question(question_prompts[7],"a"),
    Question(question_prompts[8],"b"),
    Question(question_prompts[9],"a"),
    Question(question_prompts[10],"d"),
    Question(question_prompts[11],"a"),
    #######################################
    Question(question_prompts[12], "f"),
    Question(question_prompts[13], "t"),
    Question(question_prompts[14], "f"),
    Question(question_prompts[15], "f"),
    Question(question_prompts[16], "t"),
    Question(question_prompts[17], "f"),
    Question(question_prompts[18], "t"),
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
