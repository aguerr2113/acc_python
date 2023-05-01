# Artemio Guerrero,
# complete
# Personal Information Class:
# Design a class called Employee that holds the following data about an employee:
# name
# ID number
# Department
# Job Title

class Employee:
    def __init__(self,name,id_number,department,job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
#####################################################################################

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

#####################################################################################

    def get_id_number(self):
        return self.id_number

    def set_id_number(self, id_number):
        self.id_number = id_number

#####################################################################################

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

#####################################################################################

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title

#####################################################################################
    def __str__(self):
        return f'Name: {self.name}\nID number: {self.id_number}\nDepartment: {self.department}\nTitle:{self.job_title}'



    


        

# Class. Store your class in a separate file called employee.py.
# Your class will have an initializer method that will be passed the information entered by the user as
# arguments.
# Write appropriate accessor and mutator methods for each data attribute.
# Write a __str__ method to print the contents of the class (see example of __str__ on p. 523).
