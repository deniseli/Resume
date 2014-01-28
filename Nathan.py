# This is a python script to simulate a conversation with Nathan Handler.  It
# does not pass the Turing test, but then, neither does the real Nathan, so that
# limitation exists purely for the sake of realism, and definitely has nothing
# to do with my ability to make a bot that can pass the Turing test.
#
# Denise Li
# January 2014
#
# Nathan.py

import nltk
import random
import sys


def split_text(text):
    return nltk.word_tokenize(text)

def nathan_says(text):
    print "NathanBot: " + text

def talk_about_open_source():
    nathan_is_a_pretty_big_deal("open source")

def talk_about_debian():
    nathan_is_a_pretty_big_deal("debian")

def nathan_is_a_pretty_big_deal(community):
    sayings = ["I'm a pretty big deal in the " + community + " community.",
               "Have you heard about my involvement with " + community + "?"]
    nathan_says(random.choice(sayings))

def default_nathan():
    if random.choice([1, 2]) is 1: talk_about_open_source()
    else: talk_about_debian()



input = ""
nathan_says("Oh, hi!")
while True:
    input = raw_input("> ")
    if "fuck off, nathan" in input:
        nathan_says("Oh, come on!")
        sys.exit()
    else:
        default_nathan()
