# Tuple

tup1 = (2, "Hello", "Python")
print("Tuple:", tup1)

# Accessing elements

lang = ("Python", "C", "C++")

print("First element:", lang[0])
print("Last element:", lang[-1])


# Tuple cannot be modified

# lang[2] = "Java"


# Iterating through tuple

fruits = ("apple", "banana", "orange")

print("\nTuple Elements:")

for fruit in fruits:
    print(fruit)


# count()

vowels = ("a", "e", "i", "o", "i", "u")

print("\ncount():")
print(vowels.count("i"))


# index()

print("\nindex():")
print(vowels.index("e"))


# max()

numbers = (2, 3, 4, 5, 7, 8, 9)

print("\nmax():")
print(max(numbers))


# min()

print("\nmin():")
print(min(numbers))


# sum()

print("\nsum():")
print(sum(numbers))


# len()

print("\nlen():")
print(len(numbers))


# tuple to list

mohan = (1, 22, 2, 232.33)

print("\nTuple to List:")
print(list(mohan))


# Tuple concatenation

t1 = (1, 2, 3)
t2 = (4, 5, 6)

print("\nTuple Concatenation:")
print(t1 + t2)


# Adding corresponding elements using zip()

new = []

for i, j in zip(t1, t2):
    new.append(i + j)

print("\nAdding Corresponding Elements:")
print(tuple(new))


# Tuple repetition

d = (1, 2, 3)

print("\nTuple Repetition:")
print(d * 3)


# Membership

d = (2, 3, 4, 5, 6, 6, 7, 7, 87, 88, 8)

print("\nMembership:")
print(22 in d)
print(22 not in d)


# Identity

t1 = (1, 2, 3)
t2 = (1, 2, 3, 5, 35, 34)

print("\nIdentity:")
print(t1 is not t2)


# Iterating through tuple

d = (1, 2, 3, 35, 4, 6, 7, 8)

print("\nIterating through Tuple:")

for i in d:
    print(i)


# Nested Tuple

nested = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("\nNested Tuple:")
print(nested)


# Accessing Nested Tuple

print("\nNested Tuple Element:")
print(nested[0][0])


# Searching number in nested tuple

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (2, 8, 9)
)

num = 7
exists = False

for i in matrix:
    for j in i:
        if j == num:
            exists = True

print("\nSearching in Nested Tuple:")

if exists:
    print("True")
else:
    print("False")