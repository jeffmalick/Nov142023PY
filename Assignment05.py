# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# jmalick,11/13/2023,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student: dict[str] = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.

# include json library
import json
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except Exception as e:
    print('error opening file check to make sure', FILE_NAME, 'exists.')
    print(e)
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if student_first_name == '':
                raise ValueError("Name can't be blank.")
            student_last_name = input("Enter the student's last name: ")
            if student_last_name == '':
                raise ValueError("Name can't be blank.")
            course_name = input("Please enter the name of the course: ")
            if course_name == '':
                raise ValueError("course can't be blank.")
            student = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student)
        except ValueError as e:
            print(e)
        continue
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("~-"*10)
        for student in students:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        print("~-"*10)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except Exception as e:
            print('error saving file')
            print(e)
        finally:
            if file and not file.closed:
                file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")