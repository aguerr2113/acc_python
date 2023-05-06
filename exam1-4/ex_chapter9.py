from question import Question

question_prompts = [

    "Review Questions\n\nMultiple Choice\n\n1.	You can use the ______ operator to determine whether a key exists in a dictionary.\na.	&\nb.	in\nc.	    ^\nd.	?\n\n",

    "2.	You use _____ to delete an element from a dictionary.\na.	the remove method\nb.	the erase method\nc.	the delete method\nd.	the del     statement\n\n",

    "3.	The _____ function returns the number of elements in a dictionary: \na.	size()\nb.	len()\nc.	elements()\nd.	count()\n\n",

    "4.	You can use ______ to create an empty dictionary.\na.	{}\nb.	()\nc.	[]\nd.	empty()\n\n",

    "5.	The _____ method returns a randomly selected key-value pair from a dictionary.\na.	pop()\nb.	random()\nc.	popitem()\nd.	rand_pop()\n\n",

    "6.	The _____ method returns the value associated with a specified key and removes that key-value pair from the dictionary.\na.	pop()\nb.	random()    \nc.	popitem()\nd.	rand_pop()\n\n",

    "7.	The _____ dictionary method returns the value associated with a specified key. If the key is not found, it returns a default value.\na.	pop()\nb.	    key()\nc.	value()\nd.	get()\n\n",

    "8.	The _____ method returns all of a dictionary's keys and their associated values as a sequence of tuples.\na.	keys_values()\nb.	values()\nc.	    items()\nd.	get()\n\n",

    "9.	The following function returns the number of elements in a set:\na.	size()\nb.	len()\nc.	elements()\nd.	count()\n\n",

    "10.	You can add one element to a set with this method.\na.	append\nb.	add\nc.	update\nd.	merge\n\n",

    "11.	You can add a group of elements to a set with this method.\na.	append\nb.	add\nc.	update\nd.	merge\n\n",

    "12.	This set method removes an element, but does not raise an exception if the element is not found.\na.	remove\nb.	discard\nc.	delete\nd.	    erase\n\n",

    "13.	This set method removes an element and raises an exception if the element is not found.\na.	remove\nb.	discard\nc.	delete\nd.	erase\n\n",

    "14.	This operator can be used to find the union of two sets.\na.	|\nb.	&\nc.	-\nd.	^\n\n",

    "15.	This operator can be used to find the difference of two sets.\na.	|\nb.	&\nc.	-\nd.	^\n\n",

    "16.	This operator can be used to find the intersection of two sets.\na.	|\nb.	&\nc.	-\nd.	^\n\n",

    "17.	This operator can be used to find the symmetric difference of two sets.\na.	|\nb.	&\nc.	-\nd.	^\n\n",

    "True or False\n\n1.	The keys in a dictionary must be mutable objects.(t)(f)\n",

    "2.	Dictionaries are not sequences.(t)(f)\n\n",

    "3.	A tuple can be a dictionary key.(t)(f)\n\n",

    "4.	A list can be a dictionary key.(t)(f)\n\n",

    "5.	The dictionary method popitem does not raise an exception if it is called on an empty dictionary.(t)(f)\n\n",

    "6.	The following statement creates an empty dictionary:(t)(f)\n\nmydct = {}\n\n",

    "7.	The following statement creates an empty set:(t)(f)\n\nmyset = ()\n\n",

    "8.	Sets store their elements in an unordered fashion.(t)(f)\n\n",

    "9.	You can store duplicate elements in a set.(t)(f)\n\n",

    "10.The remove method raises an exception if the specified element is not found in the set.(t)(f)\n\n",
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "c"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "a"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "b"),
    Question(question_prompts[16], "d"),
    #######################################
    Question(question_prompts[17], "f"),
    Question(question_prompts[18], "t"),
    Question(question_prompts[19], "t"),
    Question(question_prompts[20], "f"),
    Question(question_prompts[21], "t"),
    Question(question_prompts[22], "t"),
    Question(question_prompts[23], "f"),
    Question(question_prompts[24], "t"),
    Question(question_prompts[25], "f"),
    Question(question_prompts[26], "t"),
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
