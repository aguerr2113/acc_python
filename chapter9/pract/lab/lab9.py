# Artemio Guerrero
# Complete

# Write a program that creates a dictionary conaining course numbers and the room numbers of the rooms where the courses meet. The dictionary should have the following key value pairs:

# Enter a course number or press enter to stop:asdfjkl
# asdfjkl is an invalid course number.
# Enter a course number or press enter to stop: CS101
# Room: 3004
# Time: 8:00 am
# Enter a course number or press enter to stop:


course_room = {

    'CS101':"3004",
    'CS102':"4501",
    'CS103':"6755",  
    'NT101':"1244", 
    'CM210':"1411"
}
course_instr = {
    'CS101':"Haynes",
    'CS102':"Alvarado",
    'CS103':"Rich",  
    'NT101':"Burke", 
    'CM210':"Lee"
}
course_time = {
    'CS101':"8:00  am",
    'CS102':"9:00  am",
    'CS103':"10:00 am",  
    'NT101':"11:00 am", 
    'CM210':"1:00  pm"
    }
while True:
    course_number = input('Enter a course number or press enter to stop: ')
    if course_number == '':
        break
    elif course_number not in course_room:
        print(f'{course_number} is an invalid course number.')

    elif course_number in course_room:
        print(f'Room Number: {course_room[course_number]}')
        print(f'Course Instructor: {course_instr[course_number]}')
        print(f'Time: {course_time[course_number]}')