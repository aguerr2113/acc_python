from tkinter import *

# Create a window
window = Tk()

# Set the window title
window.title("Quiz")

# Set the window size
window.geometry("500x300")

# Define the question prompts and answers
question_prompts = [


    "1.	A file that data is written to is known as a(n)\na)	input file\nb)	output file\nc)	sequential access file\nd)	binary file\n\n",

  

    " 2.	A file that data is read from is known as a(n) \na)	input file\nb)	output file\nc)	sequential access file\nd)	binary file\n\n",


    "3.	Before a file can be used by a program, it must be\na)	formatted\nb)	encrypted\nc)	closed\nd)	opened\n\n",



    "4.	When a program is finished using a file, it should do this.\na)	erase the file\nb)	open the file\nc)	close the file\nd)	encrypt the file\n\n",
 
    "5.	The contents of this type of file can be viewed in an editor such as Notepad.\na)	text file\nb)	binary file\nc)	English file\nd)	human-readable file\n\n",


    " 6.	This type of file contains data that has not been converted to text.\na)	text file\nb)	binary file\nc)	Unicode file\nd)	symbolic file\n\n",


    "7.	When working with this type of file, you access its data from the beginning of the file to the end of the file.\na)	ordered access\nb)	binary access\nc)	direct access\nd)	sequential access\n\n",


    
    "8.	When working with this type of file, you can jump directly to any piece of data in the file without reading the data that comes before it.\na)	ordered access\nb)	binary access\nc)	direct access\nd)	sequential access\n\n",


    
    "9.	This is a small “holding section” in memory that many systems write data to before writing the data to a file.\na)	buffer\nb)	variable\nc)	virtual file\nd)	temporary file\n\n",

   
    "10.	This marks the location of the next item that will be read from a file.\na)	input position\nb)	delimiter\nc)	pointer\nd)	read position \n\n",


    
    "11.	When a file is opened in this mode, data will be written at the end of the file's existing contents.\na)	output mode\nb)	append mode\nc)	backup mode\nd)	read-only mode\n\n",




    "12.	This is a single piece of data within a record.\na)	fielde\nb)	variable\nc)	delimiter\nd)	subrecord\n\n",



    "13.	When an exception is generated, it is said to have been           .\na)	built\nb)	raised\nc)	caught\nd)	killed\n\n",




    "14.	This is a section of code that gracefully responds to exceptions.\na)	exception generator\nb)	exception manipulator\nc)	exception handler\nd)	exception monitor\n\n",

    
    "15.	You write this statement to respond to exceptions.\na)	run/handle\nb)	try/except\nc)	try/handle\nd)	attempt/except\n\n",



    "True or False\n16.	When working with a sequential access file, you can jump directly to any piece of data in the file without reading the data that comes before it.(t)(f)\n\n",


    "17.	When you open a file that file already exists on the disk using the 'w' mode, the contents of the existing file will be erased.(t)(f)\n\n",

    "18.	The process of opening a file is only necessary with input files. Output files are automatically opened when data is written to them.(t)(f)\n\n",
    
    "19.	When an input file is opened, its read position is initially set to the first item in the file.(t)(f)\n\n",
    

    "20.	When a file that already exists is opened in append mode, the file's existing contents are erased.(t)(f)\n\n",

    "21.	If you do not handle an exception, it is ignored by the Python interpreter, and the program continues to execute.(t)(f)\n\n",

    "22.	You can have more than one except clause in a try/except statement.(t)(f)\n\n",
    
    "23.	The else suite in a try/except statement executes only if a statement in the try suite raises an exception.(t)(f)\n\n",

    "24.	The finally suite in a try/except statement executes only if no exceptions are raised by statements in the try suite.(t)(f)\n\n",

]
answers = [
    question_prompts[0], "b",
    question_prompts[1], "a",
    question_prompts[2], "d",
    question_prompts[3], "c",
    question_prompts[4], "a",
    question_prompts[5], "b",
    question_prompts[6], "d",
    question_prompts[7], "c",
    question_prompts[8], "a",
    question_prompts[9], "c",
    question_prompts[10], "b",
    question_prompts[11], "a",
    question_prompts[12], "b",
    question_prompts[13], "c",
    question_prompts[14], "b",
    question_prompts[15], "f",
    question_prompts[16], "t",
    question_prompts[17], "f",
    question_prompts[18], "t",
    question_prompts[19], "f",
    question_prompts[20], "t",
    question_prompts[21], "t",
    question_prompts[22], "f",
    question_prompts[23], "t",
]

# Create a label for the question
question_label = Label(window, text=question_prompts[], font=("Arial", 14))
question_label.pack()

# Create a text box for the user's answer
answer_textbox = Entry(window, font=("Arial", 14))
answer_textbox.pack()

# Create a button to check the answer
def check_answer():
    user_answer = answer_textbox.get()
    if user_answer == answers[]:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect!")

check_button = Button(window, text="Check", command=check_answer, font=("Arial", 14))
check_button.pack()

# Create a label for the result
result_label = Label(window, font=("Arial", 14))
result_label.pack()

# Start the window
window.mainloop()