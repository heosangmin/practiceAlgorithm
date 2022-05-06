'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def solution(inputString):
    m = {}
    for c in inputString:
        if c not in m:
            m[c] = 0
        m[c] += 1
    
    tmp = [x % 2 for x in m.values()]
    return tmp.count(1) <= 1

print(solution("aabb")) # True
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc")) # False
print(solution("abbcabb")) # True
print(solution("zyyzzzzz")) # True
print(solution("z")) # True
print(solution("zaa")) # True
print(solution("abca")) # False
print(solution("abcad")) # False
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa")) # False
print(solution("abdhuierf")) # False
