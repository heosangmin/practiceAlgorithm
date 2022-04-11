import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

def solution(inputArray):
    maxLen = -sys.maxsize
    result = []
    for e in inputArray:
        if len(e) >= maxLen:
            maxLen = len(e)
    for e in inputArray:
        if len(e) >= maxLen:
            result.append(e)
    return result

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(inputArray))