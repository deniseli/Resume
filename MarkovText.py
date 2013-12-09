# This is a Markov chain-based text generator.  The instructions are clear when
# you run it.  This file is the second iteration of an old Java file I wrote
# several years ago, but prettier and in Python.
#
# Denise Li 2013


import nltk
import random
import os
import sys

END_PUNCTUATION = ['.', '!', '?']
NO_SPACE_BEFORE_PUNCTUATION = ['\'', '\"', '\,', ':', ')', '/', '\\', ',']
NO_SPACE_AFTER_PUNCTUATION = ['(' '/', '\\', '(']

MIN_OUTPUT_CHAR_LENGTH = 100

def split_text():
    return nltk.word_tokenize(raw_text)

def make_dict():
    global dict_has_upper
    global following_word_dict
    for i in range(0, len(word_list) - 1):
        word = word_list[i]
        next = word_list[i + 1]
        print word + " " + next
        if word.istitle() or word.isdigit():
            dict_has_upper = True
        if word in following_word_dict:
            if not next in dict[word]:
                following_word_dict[word].append(next)
        else:
            following_word_dict[word] = [next]

def print_hr():
    rows, columns = os.popen('stty size', 'r').read().split()
    print '-' * int(columns)

def choose_first_word():
    word = random.choice(following_word_dict.keys())
    while not word.istitle() and not word.isdigit() and dict_has_upper:
        word = random.choice(following_word_dict.keys())
    return word

def print_new_segment():
    word = choose_first_word()
    sentence = word
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

def input_line():
    return raw_input("Enter the line of text you would like to reorder:\n> ")

def input():
    sys.stdout.write("Enter the block of text you would like to reorder." +
                     "Press ENTER, then CTRL + D when you are done.\n> ")
    s = sys.stdin.read()
    return s

raw_text = input()
word_list = split_text()
dict_has_upper = False
following_word_dict = {}
make_dict()
print_hr()
print_new_segment()
print_hr()
