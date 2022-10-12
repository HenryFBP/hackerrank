#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true


import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s: str) -> str:
    # Write your code here
    # remove spaces
    s = s.replace(' ', '')
    L = len(s)

    # get grid size
    grid_factor: float = math.sqrt(L)

    rows = math.floor(grid_factor)
    columns = math.ceil(grid_factor)

    # ensure rows x columns >= L
    assert ((rows * columns) >= L)

    ret = ""

    for r in range(0, rows):
        for c in range(0, columns):

            # Index our string `s` like it's a 2d array
            idx = r + (rows * c)

            ret += s[idx]

            # time to add ' '
            if c == rows:
                ret += ' '

    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # result = encryption(s)
    #
    # fptr.write(result + '\n')
    #
    # fptr.close()

    assert (
            encryption(
                'if man was meant to stay on the ground god would have given us roots'
            ) == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'
    )
