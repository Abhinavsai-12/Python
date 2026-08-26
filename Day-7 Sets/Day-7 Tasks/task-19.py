# # Python Sets - Complete Practice File


# 1. Creating a Set
my_set = {1, 2, 3, 4}
# print("Original Set:")
# print(my_set)


# # 2. add()
# my_set.add(5)
# print("\nAfter add():")
# print(my_set)


# # 3. update()
# my_set.update([6, 7, 8])
# print("\nAfter update():")
# print(my_set)


# # 4. remove()
# my_set.remove(8)
# print("\nAfter remove():")
# print(my_set)


# # 5. discard()
# my_set.discard(7)

# print("\nAfter discard():")
# print(my_set)


# # 6. pop()
# removed_element = my_set.pop()
# print("\nAfter pop():")
# print("Removed element:", removed_element)
# print("Set:", my_set)


# # 7. clear()
# my_set.clear()
# print("\nAfter clear():")
# print(my_set)


# # Creating Sets for Set Operations

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# print("\nSet A:")
# print(A)

# print("Set B:")
# print(B)


# # 8. Union

# print("\nUnion using |:")
# print(A | B)

# print("Union using union():")
# print(A.union(B))


# # 9. Intersection

# print("\nIntersection using &:")
# print(A & B)

# print("Intersection using intersection():")
# print(A.intersection(B))


# # 10. Difference

# print("\nDifference A - B:")
# print(A - B)

# print("Difference using difference():")
# print(A.difference(B))

# print("\nDifference B - A:")
# print(B - A)


# # 11. Symmetric Difference

# print("\nSymmetric Difference using ^:")
# print(A ^ B)

# print("Symmetric Difference using method:")
# print(A.symmetric_difference(B))


# # 12. Membership

# print("\nMembership Test:")

# print(3 in A)

# print(10 in A)

# print(10 not in A)


# # 13. Copy

# C = A.copy()

# print("\nCopy of A:")
# print(C)


# # 14. isdisjoint()

# X = {1, 2, 3}
# Y = {4, 5, 6}

# print("\nDisjoint Test:")
# print(X.isdisjoint(Y))


# # 15. issubset()

# X = {1, 2}
# Y = {1, 2, 3, 4}

# print("\nSubset Test:")
# print(X.issubset(Y))


# # 16. issuperset()

# print("\nSuperset Test:")
# print(Y.issuperset(X))



# # 17. intersection_update()

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A.intersection_update(B)
# print("\nAfter intersection_update():")
# print(A)




# # 20. Loop Through a Set
# numbers = {10, 20, 30, 40}
# print("\nLoop Through Set:")
# for number in numbers:
#     print(number)



# # 21. Length of Set
# print("\nLength of Set:")
# print(len(numbers))


# #Frozenset
# numbers = frozenset([1, 2, 3, 4])
# print("\nFrozenset:")
# print(numbers)


