import os
import random

base_dir = os.path.dirname(__file__)
input_file_path = os.path.join(base_dir, "input.txt")
output_file_path = os.path.join(base_dir, "output.txt")

ques = """How many such pairs of letters are there in the words 'WORD_TO_REPLACE' (when counted in forward i.e. A-Z and backward direction Z-A) which have as many letters between them in the word as there are in English alphabetical order?\n (a) One  (b) Two  (c) Three  (d) More Than three\n"""

def get_alphabets():
	return [ chr(i) for i in range(97,123)]

def get_letter_indexes(word, alphabets):
	return [alphabets.index(i.lower()) for i in word]

def get_letters_pairs(word, letters_pairs_lst, backward=False):
    alphabets = get_alphabets()
    indexes = get_letter_indexes(word, alphabets)
    res = [[indexes[i], indexes[i + 1]]
        for i in range(len(indexes) - 1)]
    for i in res:
        if i[1]-i[0] == 1:
            letters_pairs_lst.append(alphabets[i[0]]+alphabets[i[1]])
    if not backward:
        get_letters_pairs(word[::-1], letters_pairs_lst, True)

def verify_pairs_letters(word):
    letters_pairs_lst = []
    get_letters_pairs(word, letters_pairs_lst)
    if not letters_pairs_lst or len(letters_pairs_lst) != len(set(letters_pairs_lst)):
        return False
    else:
        return True

def read_input_file(path):
    with open(path) as f:
        contents = f.readlines()
        words = contents[0].split(",")
        for i in words:
            if verify_pairs_letters(i):
                word_lst.append(i)

def gen_output(path):
    with open(path, "w") as f:
        for ind, i in enumerate(random_words):
            question = ques.replace('WORD_TO_REPLACE', i)
            f.write(f"{question}")

word_lst = []

read_input_file(input_file_path)
random_words = random.sample(word_lst, 5)
gen_output(output_file_path)

