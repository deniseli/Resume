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

def talk_about_paul():
    sayings = ["Did you meet Paul Tagliamonte at R|P? He's @paultag on GitHub."]
    nathan_says(random.choice(sayings))

def default_nathan():
    rand = random.randint(0, 2)
    if rand is 0:   talk_about_open_source()
    elif rand is 1: talk_about_debian()
    elif rand is 2: talk_about_paul()


input = ""
nathan_says("Oh, hi!")
while True:
    input = raw_input("> ").lower()
    if "fuck off, nathan" in input:
        nathan_says("Oh, come on!")
        sys.exit()
    elif "paul tagliamonte" in input or "paultag" in input:
        talk_about_paul()
    else:
        default_nathan()
