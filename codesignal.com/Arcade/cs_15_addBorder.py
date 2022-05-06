'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''

def solution(picture):
    return ["*" * (len(picture[0])+2)] + ["*"+s+"*" for s in picture] + ["*" * (len(picture[0])+2)]

print(solution(["abc","ded"]))