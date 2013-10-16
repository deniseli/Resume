import nltk
import random
import os

END_PUNCTUATION = ['.', '!', '?']
NO_SPACE_BEFORE_PUNCTUATION = ['\'', '\"', '\,', ':', ')', '/', '\\', ',']
NO_SPACE_AFTER_PUNCTUATION = ['(' '/', '\\', '(']

MIN_OUTPUT_LENGTH = 100

def split_text():
    return nltk.word_tokenize(raw_text)

def make_dict():
    dict = {}
    for i in range(0, len(word_list) - 1):
        word = word_list[i]
        next = word_list[i + 1]
        if word in dict:
            if not next in dict[word]:
                dict[word].append(next)
        else:
            dict[word] = [next]
    return dict

def print_hr():
    rows, columns = os.popen('stty size', 'r').read().split()
    print '-' * int(columns)

def print_new_sentence():
    # Choose first word
    word = random.choice(following_word_dict.keys())
    while (word[0] < 'A' or word[0] > 'Z') and (word[0] < '0' or word[0] > '9'):
        word = random.choice(following_word_dict.keys())
    sentence = word
    # Fill in more words until sentence completion.
    while not sentence[-1] in END_PUNCTUATION or \
          len(sentence) < MIN_OUTPUT_LENGTH:
        word = random.choice(following_word_dict[word])
        if not word[0] in END_PUNCTUATION + NO_SPACE_BEFORE_PUNCTUATION and \
           not word[-1] in NO_SPACE_AFTER_PUNCTUATION:
            sentence += " "
        sentence += word
    print sentence

raw_text = raw_input("Enter the block of text you would like to reorder:\n> ")
word_list = split_text()
following_word_dict = make_dict()
print_hr()
print_new_sentence()
print_hr()
