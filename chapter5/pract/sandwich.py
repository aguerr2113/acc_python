# Instructions for making a sandwich .
# this is a program that show how to make a sandwich. 
# The main function
# a. Displays an intro message to the user (Ex.– “Hello this is how you make a
# sandwich”)
# b. Calls the step1 function
# c. Calls the step2 function
# d. Calls all remaining step functions
# e. Displays an exit message on a new line (Ex. – “Goodbye”)
# 

def sand_prompt():
    print('Hello this is how you make a sandwich\n')

# 2. Step1 function displays step1

def step1():
    print('Step 1:Go to kitchen\n')
# 3. Step2 function displays step2 … etc.s
def step2():
    print('Step 2:Get a plate\n')

def step3():
    print('step 3:Get 2 slices of bread\n')

def step4():
    print('step 4:Get 1 slice of ham\n')

def step5():
    print('step 5:Get 1 slice of cheese\n')

def step6():
    print('step 6:Lay ingrediants on plate\n')

def step7():
    print('step 7:Place slices of bread flat side by side\n')

def step8():
    print('step 8:Place 1 slice of ham on one slice of bread\n')   

def step9():
    print('step 9:Place 1 slice of cheese on the one slice of ham.So the layer is bread,ham,cheese.\n')

def step10():
    print('step 10:Place bread slice with nothing on it on the layer of cheese.The layers should now be Bread,ham,cheese,bread\n')
def step11():
    print('step 11:you have now completed your dry bland sandwich enjoy!\n')


# a. Displays an intro message to the user (Ex.– “Hello this is how you make a
# sandwich”)
# b. Calls the step1 function
# c. Calls the step2 function
# c. Calls the step3-11 function
def sandwich():
    sand_prompt()
    
    input('Press Enter to see Step 1.\n')
    step1()
    
    input('Press Enter to see Step 2.\n')
    step2()

    input('Press Enter to see Step 3.\n')
    step3()

    input('Press Enter to see Step 4.\n')
    step4()

    input('Press Enter to see Step 5.\n')
    step5()

    input('Press Enter to see Step 6.\n')
    step6()

    input('Press Enter to see Step 7.\n')
    step7()

    input('Press Enter to see Step 8.\n')
    step8()

    input('Press Enter to see Step 9.\n')
    step9()

    input('Press Enter to see Step 10.\n')
    step10()

    input('Press Enter to see Step 11.\n')
    step11()
    # Displays an exit message on a new line (Ex. – “Goodbye”)
    print("Goodbye!")

sandwich()
