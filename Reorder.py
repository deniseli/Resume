import nltk
import random
import os

END_PUNCTUATION = ['.', '!', '?']
NO_SPACE_BEFORE_PUNCTUATION = ['\'', '\"', '\,', ':', ')', '/', '\\', ',']
NO_SPACE_AFTER_PUNCTUATION = ['(' '/', '\\', '(']

MIN_OUTPUT_CHAR_LENGTH = 100

def split_text():
    return nltk.word_tokenize(raw_text)

def make_dict():
    global dict_has_upper
    dict = {}
    for i in range(0, len(word_list) - 1):
        word = word_list[i]
        next = word_list[i + 1]
        if word.istitle() or word.isdigit():
            dict_has_upper = True
        if word in dict:
            if not next in dict[word]:
                dict[word].append(next)
        else:
            dict[word] = [next]
    return dict

def print_hr():
    rows, columns = os.popen('stty size', 'r').read().split()
    print '-' * int(columns)

def choose_first_word():
    word = random.choice(following_word_dict.keys())
    while not word.istitle() and not word.isdigit() and dict_has_upper:
        word = random.choice(following_word_dict.keys())
    return word

def print_new_segment():
    # Choose first word
    word = choose_first_word()
    sentence = word
    # Fill in more words until sentence completion.
    while not sentence[-1] in END_PUNCTUATION or \
          len(sentence) < MIN_OUTPUT_CHAR_LENGTH:
        if not word in following_word_dict:
            word = choose_first_word()
            if not sentence[-1] is '.':
                sentence += "."
        else:
            word = random.choice(following_word_dict[word])
        if not word[0] in END_PUNCTUATION + NO_SPACE_BEFORE_PUNCTUATION and \
           not word[-1] in NO_SPACE_AFTER_PUNCTUATION:
            sentence += " "
        sentence += word
    print sentence

raw_text = raw_input("Enter the block of text you would like to reorder:\n> ")
word_list = split_text()
dict_has_upper = False
following_word_dict = make_dict()
print_hr()
print_new_segment()
print_hr()
