import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

def solution(s1, s2):
    c1 = {}
    c2 = {}
    result = 0

    for c in s1:
        if c in c1:
            c1[c] += 1
        else:
            c1[c] = 1

    for c in s2:
        if c in c2:
            c2[c] += 1
        else:
            c2[c] = 1

    for key in c1:
        if key in c2:
            result += min(c1[key], c2[key])
    
    return result

s1 = "aabcc"
s2 = "adcaa"

print(solution(s1,s2))

'''
다음과 같이 리스트컴프리헨션으로 한 번에 처리 가능함.
return sum(min(s1.count(x), s2.count(x)) for x in set(s1))
'''