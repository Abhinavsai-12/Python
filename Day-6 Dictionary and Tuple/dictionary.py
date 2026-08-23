thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)


print("\n2. Changing Dictionary Value")
thisdict["year"] = 1965
print(thisdict)


print("\n3. Dictionary Length")
print(len(thisdict))



print("\n4. Accessing Dictionary Items")
x = thisdict["model"]
print("Using []:", x)
x = thisdict.get("model")
print("Using get():", x)



print("\n5. keys()")
x = thisdict.keys()
print(x)
print("Dictionary Keys:")


for key in thisdict.keys():
    print(key)



print("\n6. values()")
x = thisdict.values()
print(x)

print("Dictionary Values:")
for value in thisdict.values():
    print(value)


print("\n7. items()")
x = thisdict.items()
print(x)

print("Key-Value Pairs:")
for key, value in thisdict.items():
    print(key, "->", value)


print("\n8. update()")
thisdict.update({"year": 2020})
print(thisdict)


print("\n9. Adding Items")
thisdict["color"] = "Red"
print(thisdict)

print("\n10. pop()")
thisdict.pop("model")
print(thisdict)

print("\nAdding model again")
thisdict["model"] = "Mustang"
print(thisdict)

print("\n12. popitem()")
thisdict.popitem()
print(thisdict)

print("\nAdding color again")
thisdict["color"] = "Red"
print(thisdict)

print("\n14. del")
del thisdict["color"]
print(thisdict)

print("\nAdding color again")
thisdict["color"] = "Red"
print(thisdict)

print("\n16. clear()")
thisdict.clear()
print(thisdict)

print("\n17. Creating Dictionary Again")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


print("\n18. Loop Through Keys")
for x in thisdict:
    print(x)


print("\n19. Loop Through Values")
for x in thisdict:
    print(thisdict[x])


print("\n20. Loop Through Keys Using keys()")
for x in thisdict.keys():
    print(x)


print("\n21. Loop Through Values Using values()")
for x in thisdict.values():
    print(x)


print("\n22. Loop Through Key-Value Pairs")
for key, value in thisdict.items():
    print(key, "->", value)


