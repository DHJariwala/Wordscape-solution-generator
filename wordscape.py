import nltk
from itertools import combinations

nltk.download('words')


def is_english_word(string):
    if string in words.words():
        return 1
    return 0


def find_words(toFind):
    wordsList = []
    nums = list(toFind)
    permutations = list(itertools.permutations(nums))
    permutes = [''.join(permutation) for permutation in permutations]
    for word in permutes:
        if is_english_word(word):
            wordsList.append(word)
            pass
        pass
    return wordsList


def print_list(l):
    for x in l:
        for i in x:
            print(str(len(i)) + "  " + str(i))
            pass
        pass
    pass


def all_existing_words(x, print_combinations = False):
    allCombinations = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
    existingWords = []
    for i in allCombinations:
        if print_combinations:
            print("current combination: " + i)
            existingWords.append(find_words(i))
        else:
            existingWords.append(find_words(i))
        pass
    print_list(existingWords)
    pass


x = input("Enter letters without space: ").lower()
all_existing_words(x,True)