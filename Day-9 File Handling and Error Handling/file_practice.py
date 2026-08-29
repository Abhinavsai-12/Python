# Create and write

with open("student.txt", "w") as file:
    file.write("Name: Abhinav\n")
    file.write("Course: Python\n")
    file.write("Marks: 85\n")


# Read

with open("student.txt", "r") as file:
    data = file.read()

print("File Content:")
print(data)


# Append

with open("student.txt", "a") as file:
    file.write("Status: Pass\n")


# Read again

with open("student.txt", "r") as file:
    data = file.read()

print("Updated File:")
print(data)