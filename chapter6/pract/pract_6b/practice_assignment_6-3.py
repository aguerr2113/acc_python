# Write a program that uses the file, students.txt. The file contains several records. Each record contains two fields: 
# 1) the student’s name and 
# 2) the student’s score for the final exam.
# 2. Your program should read in each record in students.txt using a loop.
# 3. While in the loop, the program should display name and score
# 4. Sample output:
# Name               Score
# --------------------------------
# Jim Smith          99.0
# Mario Alvarez     100.0
# Mary Maldonado      9.0
# Bess Robinson      77.0
# Eddie Nguyen       87.0
# Turn in your program to the practice assignment link in course content.

def main():

    # Open the file
    students_file = open("students.txt", "r")

    # Print header
    print("Name\t\t\tScore")
    print("--------------------------------")

    # Loop through each line in the file
    while True:
        # Read the name
        name = students_file.readline().strip()

        # Exit the loop
        if name == "":
            break

        # Read the score and convert it to a float
        score_str = students_file.readline().strip()
        try:
            score = float(score_str)
        except ValueError:
            print(f"Error: could not convert score to float for student {name}")
            continue

        # Print the name and score
        print(f"{name.ljust(25)}{score}")

    # Close the file
    students_file.close()


if __name__ == '__main__':
    main()
