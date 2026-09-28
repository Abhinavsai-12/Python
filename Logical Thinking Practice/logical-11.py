# Python Program to Remove Punctuation



punctuations = '''!@#$%^&*(_+=-){}[];:'",.?/~'''

input_str = input("Enter the String")

new_str =""

for c in input_str:
    if c  not in punctuations:
        new_str += c

print(new_str)

