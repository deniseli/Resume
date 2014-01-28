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
import urllib2


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

def talk_about_country_music():
    # Could do something interesting with this with a web app.  Perhaps autoplay a song
    # at the top of the country music charts?
    nathan_says("Let's listen to country music!")

def talk_about_my_spirit_animal():
    # Still working on this
    nathan_says("Paul Tagliamonte is my spirit animal!")

def default_nathan():
    random.choice([
        talk_about_open_source,
        talk_about_debian,
        talk_about_paul,
        talk_about_country_music,
        talk_about_my_spirit_animal
    ])()

input = ""
input_split = []
nathan_says("Oh, hi!")
# "Oh, hi!" is temporary.  I actually want the user to input a background music
# choice upon starting NathanBot, but as soon as it loads, NathanBot replaces
# said choice with country music.
while True:
    input = raw_input("> ").lower()
    input_split = split_text(input)
    if "fuck off, nathan" in input:
        nathan_says("Oh, come on!")
        sys.exit()
    elif "paul tagliamonte" in input or "paultag" in input:
        talk_about_paul()
    else:
        default_nathan()
