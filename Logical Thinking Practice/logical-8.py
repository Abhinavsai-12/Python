# Input String is Palindrome or not


# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if reverse == original:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")








# string = input("Enter a string: ")

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")








def is_palindrome(string):
    return string == string[::-1]


string = input("Enter a string: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")