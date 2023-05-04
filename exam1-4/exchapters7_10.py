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


    "Review Questionsn\n\nMultiple Choicen\n\n1.	This is the first index in a string.n\nA.	-1n\nB.	1n\nC.	0n\nD.	The size of the string minus    onen\n\n",

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
print(len(question_prompts))

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
    Question(question_prompts[9], "b"),
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
    Question(question_prompts[19], "t"),
    Question(question_prompts[20], "f"),
    Question(question_prompts[21], "t"),
    Question(question_prompts[22], "t"),
    Question(question_prompts[23], "f"),
    #####################################
    Question(question_prompts[24], "c"),
    Question(question_prompts[25], "d"),
    Question(question_prompts[26], "b"),
    Question(question_prompts[27], "c"),
    Question(question_prompts[28], "a"),
    Question(question_prompts[29], "c"),
    Question(question_prompts[30], "d"),
    Question(question_prompts[31], "a"),
    Question(question_prompts[32], "b"),
    Question(question_prompts[33], "b"),
    #################################
    Question(question_prompts[34], "t"),
    Question(question_prompts[35], "t"),
    Question(question_prompts[36], "t"),
    Question(question_prompts[37], "t"),
    Question(question_prompts[38], "f"),
    #####################################
    Question(question_prompts[39], "b"),
    Question(question_prompts[40], "d"),
    Question(question_prompts[41], "b"),
    Question(question_prompts[42], "a"),
    Question(question_prompts[43], "c"),
    Question(question_prompts[44], "a"),
    Question(question_prompts[45], "d"),
    Question(question_prompts[46], "c"),
    Question(question_prompts[47], "b"),
    Question(question_prompts[48], "b"),
    Question(question_prompts[49], "c"),
    Question(question_prompts[50], "b"),
    Question(question_prompts[51], "a"),
    Question(question_prompts[52], "a"),
    Question(question_prompts[53], "c"),
    Question(question_prompts[54], "b"),
    Question(question_prompts[55], "d"),
    #######################################
    Question(question_prompts[56], "f"),
    Question(question_prompts[57], "t"),
    Question(question_prompts[58], "t"),
    Question(question_prompts[59], "f"),
    Question(question_prompts[60], "t"),
    Question(question_prompts[61], "t"),
    Question(question_prompts[62], "f"),
    Question(question_prompts[63], "t"),
    Question(question_prompts[64], "f"),
    Question(question_prompts[65], "t"),
    #######################################
    Question(question_prompts[66], "a"),
    Question(question_prompts[67], "d"),
    Question(question_prompts[68], "c"),
    Question(question_prompts[69], "d"),
    Question(question_prompts[70], "b"),
    Question(question_prompts[71], "d"),
    Question(question_prompts[72], "c"),
    Question(question_prompts[73], "a"),
    Question(question_prompts[74], "b"),
    Question(question_prompts[75], "a"),
    Question(question_prompts[76], "d"),
    Question(question_prompts[77], "a"),
    #######################################
    Question(question_prompts[78], "f"),
    Question(question_prompts[79], "t"),
    Question(question_prompts[80], "f"),
    Question(question_prompts[81], "f"),
    Question(question_prompts[82], "t"),
    Question(question_prompts[83], "f"),
    Question(question_prompts[84], "t"),
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
