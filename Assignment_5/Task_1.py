# Task 1: Create a Dictionary of Student Marks

# Creating the dictionary
student_marks = {
    "Amit": 85,
    "Priya": 92,
    "Ravi": 76,
    "Sneha": 89,
    "Karan": 70
}

# Asking user for input
student_name = input("Enter the student's name: ")

# Checking and displaying marks
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Student named '{student_name}' not found in the records.")
