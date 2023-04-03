# Chapter5

# Algorithm Workbench
# 1.	Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

# def times_ten(num):
#     return num * 10

# 2.	Examine the following function header, then write a statement that calls the function, passing 12 as an argument.

#  def show_value(quantity):

# show_value(12)

# 3.	Look at the following function header:

#  def my_function(a, b, c):
# Now look at the following call to my_function:

#  my_function(3, 2, 1)
# When this call executes, what value will be assigned to a? What value will be assigned to b? What value will be assigned to c?
# 3.	The values assigned to a, b, and c when calling my_function(3, 2, 1) will be:
# a = 3 b = 2 c = 1


# 4.	What will the following program display?

#  def main():
#      x = 1
#      y = 3.4
#      print(x, y)
#      change_us(x, y)
#      print(x, y)
#  def change_us(a, b):
#      a = 0
#      b = 0
#      print(a, b)
#  main()

# 1 3.4
# 0 0
# 1 3.4
# 5.	Look at the following function definition:

#  def my_function(a, b, c):
#      d = (a + c) / b
#      print(d)
# a)	Write a statement that calls this function and uses keyword arguments to pass 2 into a, 4 into b, and 6 into c.
# my_function(a=2, b=4, c=6)

# b)	What value will be displayed when the function call executes?
# The value displayed when the function call executes will be 2.0.

# 6.	Write a statement that generates a random number in the range of 1 through 100 and assigns it to a variable named rand.
# Generating a random number between 1 and 100 and assigning it to a variable named rand:
# import random
# rand = random.randint(1, 100)

# The following statement calls a function named half, which returns a value that is half that of the argument. (Assume the number variable references a float value.) Write code for the function.

#  result = half(number)
# 7.	A program contains the following function definition:

#  def cube(num):
#      return num * num * num
# Write a statement that passes the value 4 to this function and assigns its return value to the variable result.
# Function call to cube with argument 4:
# result = cube(4)


# 8.	Write a function named times_ten that accepts a number as an argument. When the function is called, it should return the value of its argument multiplied times 10.
# Function definition for times_ten:
# def times_ten(num):
#     return num * 10

# 9.	Write a function named get_first_name that asks the user to enter his or her first name, and returns it.
# Function definition for get_first_name:
# def get_first_name():
#     first_name = input("Please enter your first name: ")
#     return first_name



# 1.	A group of statements that exist within a program for the purpose of performing a specific task is a(n)           .c

# a)	block

# b)	parameter

# c)	function

# d)	expression

# 2.	A design technique that helps to reduce the duplication of code within a program and is a benefit of using functions is           .a

# a)	code reuse

# b)	divide and conquer

# c)	debugging

# d)	facilitation of teamwork

# 3.	The first line of a function definition is known as the           .d

# a)	body

# b)	introduction

# c)	initialization

# d)	header

# 4.	You            a function to execute it.b

# a)	define

# b)	call

# c)	import

# d)	export

# 5.	A design technique that programmers use to break down an algorithm into functions is known as           .a

# a)	top-down design

# b)	code simplification

# c)	code refactoring

# d)	hierarchical subtasking

# 6.	A            is a diagram that gives a visual representation of the relationships between functions in a program.d

# a)	flowchart

# b)	function relationship chart

# c)	symbol chart

# d)	hierarchy chart

# 7.	The                 keyword is ignored by the Python interpreter and can be used as a placeholder for code that will be written later.b

# a)	placeholder

# b)	pass

# c)	pause

# d)	skip

# 8.	A            is a variable that is created inside a function.b

# a)	global variable

# b)	local variable

# c)	hidden variable

# d)	none of the above; you cannot create a variable inside a function

# 9.	A(n)            is the part of a program in which a variable may be accessed.c

# a)	declaration space

# b)	area of visibility

# c)	scope

# d)	mode

# 10.	A(n)            is a piece of data that is sent into a function.a

# a)	argument

# b)	parameter

# c)	header

# d)	packet

# 11.	A(n)            is a special variable that receives a piece of data when a function is called.b

# a)	argument

# b)	parameter

# c)	header

# d)	packet

# 12.	A variable that is visible to every function in a program file is a           .d

# a)	local variable

# b)	universal variable

# c)	program-wide variable

# d)	global variable

# 13.	When possible, you should avoid using            variables in a program.b

# a)	local

# b)	global

# c)	reference

# d)	parameter

# 14.	This is a prewritten function that is built into a programming language.b

# a)	standard function

# b)	library function

# c)	custom function

# d)	cafeteria function

# 15.	This standard library function returns a random integer within a specified range of values.b

# a)	random

# b)	randint

# c)	random_integer

# d)	uniform

# 16.	This standard library function returns a random floating-point number in the range of 0.0 up to 1.0 (but not including 1.0).a

# a)	random

# b)	randint

# c)	random_integer

# d)	uniform

# 17.	This standard library function returns a random floating-point number within a specified range of values.d

# a)	random

# b)	randint

# c)	random_integer

# d)	uniform

# 18.	This statement causes a function to end and sends a value back to the part of the program that called the function.d

# a)	end

# b)	send

# c)	exit

# d)	return

# 19.	This is a design tool that describes the input, processing, and output of a function.b

# a)	hierarchy chart

# b)	IPO chart

# c)	datagram chart

# d)	data processing chart

# 20.	This type of function returns either True or False.c

# a)	Binary

# b)	true_false

# c)	Boolean

# d)	logical

# 21.	This is a math module function.c

# a)	derivative

# b)	factor

# c)	sqrt

# d)	differentiate


# True or False
# 1.	The phrase “divide and conquer” means that all of the programmers on a team should be divided and work in isolation.
# false

# 2.	Functions make it easier for programmers to work in teams.t
# true
# 3.	Function names should be as short as possible.
# false
# 4.	Calling a function and defining a function mean the same thing.
# false
# 5.	A flowchart shows the hierarchical relationships between functions in a program.
# true
# 6.	A hierarchy chart does not show the steps that are taken inside a function.
# false
# 7.	A statement in one function can access a local variable in another function.
# false
# 8.	In Python, you cannot write functions that accept multiple arguments.
# false
# 9.	In Python, you can specify which parameter an argument should be passed into a function call.
# true
# 10.	You cannot have both keyword arguments and non-keyword arguments in a function call.
# false
# 11.	Some library functions are built into the Python interpreter.
# true
# 12.	You do not need to have an import statement in a program to use the functions in the random module.
# false
# 13.	Complex mathematical expressions can sometimes be simplified by breaking out part of the expression and putting it in a function.
# True	
# 14.	A function in Python can return more than one value.
# True	
# 15.	IPO charts provide only brief descriptions of a function’s input, processing, and output, but do not show the specific steps taken in a function.
# False	


# Multiple choice chapter 6


# 1.	A file that data is written to is known as a(n)           .
# a)	output file

# 2.	A file that data is read from is known as a(n)           .
# a)	input file


# 3.	Before a file can be used by a program, it must be           .
# a)	opened

# 4.	When a program is finished using a file, it should do this.
# a)	close the file

# 5.	The contents of this type of file can be viewed in an editor such as Notepad.
# a)	text file

# 6.	This type of file contains data that has not been converted to text.
# a)	binary file

# 7.	When working with this type of file, you access its data from the beginning of the file to the end of the file.
# a)	sequential access

# 8.	When working with this type of file, you can jump directly to any piece of data in the file without reading the data that comes before it.
# a)	direct access

# 9.	This is a small “holding section” in memory that many systems write data to before writing the data to a file.
# a)	buffer

# 10.	This marks the location of the next item that will be read from a file.
# a)	pointer


# 11.	When a file is opened in this mode, data will be written at the end of the file’s existing contents.
# a)	append mode

# 12.	This is a single piece of data within a record.
# a)	field


# 13.	When an exception is generated, it is said to have been           .
# a)	raised


# 14.	This is a section of code that gracefully responds to exceptions.
# a)	exception handler


# 15.	You write this statement to respond to exceptions.
# a)	try/except




# True or False
# 16.	When working with a sequential access file, you can jump directly to any piece of data in the file without reading the data that comes before it.
# false
# 17.	When you open a file that file already exists on the disk using the 'w' mode, the contents of the existing file will be erased.
# true
# 18.	The process of opening a file is only necessary with input files. Output files are automatically opened when data is written to them.
# false
# 19.	When an input file is opened, its read position is initially set to the first item in the file.
# true
# 20.	When a file that already exists is opened in append mode, the file’s existing contents are erased.
# False
# 21.	If you do not handle an exception, it is ignored by the Python interpreter, and the program continues to execute.
# true
# 22.	You can have more than one except clause in a try/except statement.
# true
# 23.	The else suite in a try/except statement executes only if a statement in the try suite raises an exception.
# true
# 24.	The finally suite in a try/except statement executes only if no exceptions are raised by statements in the try suite.

# False



# 1.	Write a program that opens an output file with the filename my_name.txt, writes your name to the file, then closes the file.
# # Open file for writing
# output_file = open("my_name.txt", "w")

# # Write name to file
# output_file.write("Your name here\n")

# # Close file
# output_file.close()

# 2.	Write a program that opens the my_name.txt file that was created by the program in problem 1, reads your name from the file, displays the name on the screen, then closes the file.
# # Open file for reading
# input_file = open("my_name.txt", "r")

# # Read name from file
# name = input_file.readline()

# # Print name to screen
# print(name)

# # Close file
# input_file.close()

# 3.	Write code that does the following: opens an output file with the filename number_list.txt, uses a loop to write the numbers 1 through 100 to the file, then closes the file.
# # Open file for writing
# output_file = open("number_list.txt", "w")

# # Loop through numbers 1-100 and write to file
# for i in range(1, 101):
#     output_file.write(str(i) + "\n")

# # Close file
# output_file.close()

# 4.	Write code that does the following: opens the number_list.txt file that was created by the code you wrote in question 3, reads all of the numbers from the file and displays them, then closes the file.
# # Open file for reading
# input_file = open("number_list.txt", "r")

# # Read numbers from file and display them
# for line in input_file:
#     print(line.strip())

# # Close file
# input_file.close()

# 5.	Modify the code that you wrote in problem 4 so it adds all of the numbers read from the file and displays their total.
# # Open file for reading
# input_file = open("number_list.txt", "r")

# # Initialize sum to 0
# total = 0

# # Read numbers from file and add them to the sum
# for line in input_file:
#     total += int(line.strip())

# # Display total sum
# print("Total sum:", total)

# # Close file
# input_file.close()

# 6.	Write code that opens an output file with the filename number_list.txt, but does not erase the file’s contents if it already exists.
# # Open file for appending
# output_file = open("number_list.txt", "a")

# # Loop through numbers 101-200 and append to file
# for i in range(101, 201):
#     output_file.write(str(i) + "\n")

# # Close file
# output_file.close()

# 7.	A file exists on the disk named students.txt. The file contains several records, and each record contains two fields: (1) the student’s name, and (2) the student’s score for the final exam. Write code that deletes the record containing “John Perz” as the student name.
# # Open file for reading and writing
# input_file = open("students.txt", "r")
# output_file = open("students_new.txt", "w")

# # Loop through records and copy all except the one to delete
# for line in input_file:
#     if not "John Perz" in line:
#         output_file.write(line)

# # Close files
# input_file.close()
# output_file.close()

# # Delete original file
# import os
# os.remove("students.txt")

# # Rename new file
# os.rename("students_new.txt", "students.txt")

# 8.	A file exists on the disk named students.txt. The file contains several records, and each record contains two fields: (1) the student’s name, and (2) the student’s score for the final exam. Write code that changes Julie Milan’s score to 100.
# # Open file for reading and writing
# input_file = open("students.txt", "r")
# output_file = open("students_new.txt", "w")

# # Loop through records and update score for Julie Milan
# for line in input_file:
#     if "Julie Milan" in line:
#         parts = line.split(",")
#         parts[1] = "100\n"
#         line = ",".join(parts)
#     output_file.write(line)

# # Close files
# input_file.close()
# output_file.close()

# # Delete original file
# import os
# os.remove("students.txt")

# # Rename new file
# os.rename("students_new.txt", "students.txt")

# 9.	What will the following code display?

#  try:
#    x = float('abc123')
#    print('The conversion is complete.')
#  except IOError:
#    print('This code caused an IOError.')
#  except ValueError:
#    print('This code caused a ValueError.')
#  print('The end.')
# 9.	This code will display "This code caused a ValueError. The end." because float('abc123') will raise a ValueError.

# 10.	What will the following code display?

#  try:
#    x = float('abc123')
#    print(x)
#  except IOError:
#    print('This code caused an IOError.')
#  except ZeroDivisionError:
#    print('This code caused a ZeroDivisionError.')
#  except:
#    print('An error happened.')
#  print('The end.')

# 10.This code will display "An error happened. The end." because float('abc123') will raise a ValueError, but it is not handled by any of the specific except blocks. The generic except block at the end will catch it and display "An error happened."





