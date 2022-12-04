# DirtyPan.py
#
# author: B. Stone
# date: December 2015

# Program to scrub a dirty pan, clean.

import random

dirty = True # state of the pan
scrubCount = 0 # number of scrubs

while dirty:
    scrubCount += 1
    print("Scrub the pan: {}".format(scrubCount))
    print("Rinse & check if the pan is clean.")
    if not random.randint(0,9):
        print("All clean!")
        dirty = False
    else:
        print("Still dirty...")


# Test assertions:
