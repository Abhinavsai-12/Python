# Prime Number or Not


# num = int(input("Enter a number: "))
# count = 0


# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")




# num = int(input("Enter a number: "))

# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")














def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")




















