from question import Question

question_prompts = [

    "1.	This term refers to an individual item in a list.\nA.	element\nB.	bin\nC.	cubbyhole\nD.	slot\n\n",

    "2.	This is a number that identifies an item in a list.\nA.	element\nB.	index\nC. bookmark\nD.	identifier\n\n",

    "3.	This is the first index in a list.\nA.	-1\nB.	1\nC. 0\nD.	The size of the list minus one\n\n",

    "4.	This is the last index in a list.\nA. 1\nB.	99\nC.	0\nD.	The size of the list minus one\n\n",
    
    "5.	This will happen if you try to use an index that is out of range for a list.\nA.    A ValueError exception will occur.\nB.	An IndexError exception will occur.\nC.	The list will be erased and the program will continue to run.\nD.	Nothing—the invalid index will be ignored.\n\n",

    "6.	This function returns the length of a list.\nA.	length\nB.	size\nC.	len\nD.	lengthof\n\n",

    "7.	When the * operator's left operand is a list and its right operand is an integer, the operator becomes this.\nA.	The multiplication operator\nB.	The repetition operator\nC.	The initialization operator\nD.	Nothing—the operator does not support those types of operands.\n",

    "8.	This list method adds an item to the end of an existing list.\nA.	add\nB.	add_to\nC.	increase\nD.	append\n\n",

    "9.	This removes an item at a specific index in a list.\nA.	the remove method\nB.	the delete method\nC.	the del statement\nD.	the kill method\n\n",

    "10.Assume the following statement appears in a program:\n  mylist = []\n10.	Which of the following statements would you use to add the string 'Labrador' to the list at index 0?\nA.	mylist[0] = 'Labrador'\nB.	mylist.insert(0, 'Labrador')\nC.	mylist.append('Labrador')\nD.	mylist.insert('Labrador', 0)\n\n",

    "11.	If you call the index method to locate an item in a list and the item is not found, this happens.\nA.	A ValueError exception is raised.\nB.	An InvalidIndex exception is raised.\nC.	The method returns -1.\nD.	Nothing happens. The program continues running at the next statement.\n\n",

    "12.	This built-in function returns the highest value in a list.\nA.	highest\nB.	max\nC.	greatest\nD.	best_of\n\n",

    "13.	This function in the random module returns a random element from a list.\nA.	choice\nB.	choices\nC.	sample\nD.	random_element\n\n",

    "14.	This function in the random module returns multiple, nonduplicated random elements from a list.\nA.	choice\nB.	choices\nC.	sample\nD.	random_element\n\n",

    "15.	This file object method returns a list containing the file's contents.\nA.	to_list\nB.	getlist\nC.	readline\nD.	readlines\n\n",

    "16.	Which of the following statements creates a tuple?\nA.	values = [1, 2, 3, 4]\nB.	values = {1, 2, 3, 4}\nC.	values = (1)\nD.	values = (1,)\n\n",


    "True or False\n\n1.	Lists in Python are immutable.(t)(f)\n\n",

    "2.	Tuples in Python are immutable.(t)(f)\n\n",

    "3.	The del statement deletes an item at a specified index in a list.(t)(f)\n\n",
    
    "4.	Assume list1 references a list. After the following statement executes, list1 and list2 will reference two identical but separate lists in memory:\n     	list2 = list1\n(t)(f)\n\n",

    "5.	A file object's writelines method automatically writes a newline ('\n') after writing each list item to the file.(t)(f)\n\n",

    "6.	You can use the + operator to concatenate two lists.(t)(f)\n\n",

    "7.	A list can be an element in another list.(t)(f)\n\n",

    "8.	You can remove an element from a tuple by calling the tuple's remove method.(t)(f)\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "d"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "c"),
    Question(question_prompts[10],"a"),
    Question(question_prompts[11],"b"),
    Question(question_prompts[12],"a"),
    Question(question_prompts[13],"c"),
    Question(question_prompts[14],"d"),
    Question(question_prompts[15],"d"),
    ####################################
    Question(question_prompts[16], "f"),
    Question(question_prompts[17], "t"),
    Question(question_prompts[18], "t"),
    Question(question_prompts[19], "f"),
    Question(question_prompts[20], "f"),
    Question(question_prompts[21], "t"),
    Question(question_prompts[22], "t"),
    Question(question_prompts[23], "f"),
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
