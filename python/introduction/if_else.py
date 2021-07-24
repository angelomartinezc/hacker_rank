# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, n.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0:
        print("Weird")
    elif n > 1 and n < 5:
        print("Not Weird")
    elif n > 5 and n < 21:
        print("Weird")
    else:
        print("Not Weird")
