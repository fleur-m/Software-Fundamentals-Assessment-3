# EScrubPan.py
#
# author: B. Stone
# date: December 2015

# Program: Scrubbing a dirty pan.

import random

dirty = True # pan is dirty
scrubCount = 0 # number of scrubs

while dirty:
    scrubCount += 1
    print("Scrub the pan: {}".format(scrubCount))
    print("Rinse and check if the pan is clean.")
    if not random.randint(0,9):
        print("All clean!")
        dirty = False
    else:
        print("Still dirty...")


# Test assertions:
