'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

For inputString = "(bar)", the output should be
solution(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''
# import re
# def solution(inputString):
#     regex = "\(\)"
#     while re.search(regex, inputString) != None:
#         matched = re.search(regex, inputString).group()
#         inputString = inputString.replace(matched, "")
    
#     regex = "\([a-z]+\)"
#     while re.search(regex, inputString) != None:
#         matched = re.search(regex, inputString).group()
#         inputString = inputString.replace(matched, matched[len(matched)-2:0:-1])
#     return inputString

def solution(inputString):
    for i in range(len(inputString)):
        if inputString[i] == "(":
            start = i
        if inputString[i] == ")":
            end = i
            return solution(inputString[:start] + inputString[start + 1:end][::-1] + inputString[end + 1:])
    return inputString

print(solution("(bar)"))
print(solution("foo(bar)baz"))
print(solution("foo(bar)baz(blim)"))
print(solution("foo(bar(baz))blim"))
print(solution("()"))
print(solution("(())"))