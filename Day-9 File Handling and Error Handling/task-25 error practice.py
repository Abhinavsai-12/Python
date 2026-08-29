# 1. try and except

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number")









# 2. else
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a + b

except ValueError:
    print("Please enter numbers only")

else:
    print("Addition:", result)








# 3. finally
try:
    number = int(input("Enter a number: "))

    print("Number:", number)

except ValueError:
    print("Invalid input")

finally:
    print("This block always executes")









# 4. try, except, else and finally

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Calculation completed")











# 5. Handling Multiple Exceptions
try:
    numbers = [10, 20, 30]

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:
    print("Please enter an integer")

except IndexError:
    print("Index does not exist")










#Complete Example
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b == 0:
        raise ZeroDivisionError("Second number cannot be zero")

    result = a / b

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError as error:
    print("Error:", error)

else:
    print("Result:", result)

finally:
    print("Program completed")