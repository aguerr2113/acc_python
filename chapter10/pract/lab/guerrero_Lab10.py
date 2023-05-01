# Artemio Guerrero,
# complete
# Main program:
# Your main program should create three instances of the class. Your program should get the information
# from the user and pass it as parameters to the initializer method. Using the __str__ method invoked
# by the print function, the program should display the personal information for the three individuals.

import employee


def main():
    employs = make_list()

    print()
    display_list(employs)



def make_list():
    employees = []
    for count in range(1, 4):
        print()
        name = input('Enter employee name: ')
        employee_id = float(input('Enter employee ID: '))
        department = input('Enter department: ')
        job_position = input('Enter position: ')
        print()


        emp = employee.Employee(name, employee_id, department, job_position)

        employees.append(emp)

    return employees



def display_list(employees):
    count = 0
    for item in employees:
        count += 1
        print(f'Employee {count}:')
        print(str(item))
        print()

# Call the main function.
if __name__ == '__main__':
      main()