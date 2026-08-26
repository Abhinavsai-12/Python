def greet():
    print("Hello")
    print("Welcome to Python")
greet()


def greet_user(name):
    print("Hello", name)


greet_user("Abhinav")
greet_user("Kiran")
greet_user("Rahul")



def add(a, b):
    return a + b
result = add(10, 20)
print("Addition:", result)


def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(10))
print(check_even(7))


# # POSITIONAL ARGUMENTS
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student("Abhinav", 24, "Python")

# # KEYWORD ARGUMENTS
def employee(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


employee(
    name="Abhinav",
    age=24,
    department="IT"
)

# DEFAULT ARGUMENTS
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Abhinav")


# VARIABLE-LENGTH ARGUMENTS - *args
def display(*args):
    print(args)
display(10, 20, 30)
display("Python", "Java", "C++")


# Normal argument with *args
def student_marks(name, *marks):
    print("Student:", name)
    print("Marks:", marks)

student_marks("Abhinav", 80, 90, 85)


# VARIABLE-LENGTH KEYWORD ARGUMENTS - **kwargs
def display_details(**kwargs):
    print(kwargs)


display_details(
    name="Abhinav",
    age=24,
    course="Python"
)



#  LAMBDA FUNCTIONS
square = lambda x: x * x
print("Square:", square(5))


# LAMBDA WITH map()
numbers = [1, 2, 3, 4, 5]
squares = list(
    map(lambda x: x * x, numbers)
)
print("Squares:", squares)


# LAMBDA WITH filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even Numbers:", even_numbers)


# # RECURSION
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)



# NESTED FUNCTIONS
def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    inner()

outer()



# CODE REUSABILITY
# Without function:
print(10 + 20)
print(20 + 30)
print(50 + 60)


# With function:
def add(a, b):
    return a + b

print(add(10, 20))
print(add(20, 30))
print(add(50, 60))

