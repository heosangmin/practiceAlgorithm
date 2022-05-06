'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.
'''

def solution(s):
    m = {}
    for c in s:
        m[c] = True
    return len(m.keys())

print(solution("cabca")) # 3

'''
왜 이걸 생각 못했지.
return len(set(s))
'''