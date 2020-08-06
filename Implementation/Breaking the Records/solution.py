#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    m = scores[0]
    n = scores[0]
    m_count = 0
    n_count = 0
    for s in scores:
        if s > m:
            m_count += 1
            m = s
        elif s < n:
            n_count += 1
            n = s
    return m_count, n_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
