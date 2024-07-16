#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file  # Assuming this function reads and prints the file content
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

# Create an initial student instance
student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()

# Print initial student information
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

# Save the JSON representation to a file
save_to_json_file(j_student_1, path)
read_file(path)  # Assuming this function reads and prints the content of the file
print("\nSaved to disk")

# Create a new student instance (fake student)
print("\nFake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

# Load dictionary from file
print("\nLoad dictionary from file:")
new_j_student_1 = load_from_json_file(path)

# Reload attributes of new_student_1 from the loaded JSON
new_student_1.reload_from_json(new_j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
