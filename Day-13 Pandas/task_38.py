# # 1. Prime or not
# number = int(input("Enter a number: "))

# if number <= 1:
#     print("Not a prime number")
# else:
#     prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#             break

#     if prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")







# # 2.  Armstrong number or not
# number = int(input("Enter a number: "))

# original = number
# digits = len(str(number))
# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit ** digits
#     number = number // 10


# if total == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# # 3. Sum of list elements
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for number in numbers:
#     total = total + number

# print("Sum:", total)




# # 4. Sum of two lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# result = []

# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])

# print(result)




# # 5. palindrome
# # palindrome or not
# text = input("Enter a string: ")

# reverse = text[::-1]

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")





# # Palindrome number or not
# number = int(input("Enter a number: "))

# original = number
# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10


# if reverse == original:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")