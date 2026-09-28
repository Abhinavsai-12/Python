# String Permutations

def get_permutation(string, i=3):
    if i == len(string):
        print("".join(string))
        return

    for j in range(i, len(string)):
        words = [c for c in string]

        words[i], words[j] = words[j], words[i]

        get_permutation(words, i + 1)


get_permutation("Abhi")