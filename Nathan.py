# This is a python script to simulate a conversation with Nathan Handler.  It
# does not pass the Turing test, but then, neither does the real Nathan, so that
# limitation exists purely for the sake of realism, and definitely has nothing
# to do with my ability to make a bot that can pass the Turing test.
#
# Denise Li
# January 2014
#
# Nathan.py

import sys


input = ""
print "Oh, hi!"
while True:
    input = raw_input("> ")
    input = input.lower()
    if "fuck off, nathan" in input:
        sys.exit()
