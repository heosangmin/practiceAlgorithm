'''
2022/06/10

https://app.codesignal.com/interview-practice/task/dYCH8sdnxGf5aGkez

Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be
solution(s) = "abababab";

For s = "2[b3[a]]", the output should be
solution(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
solution(s) = "zyzzzabcabc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string encoded as described above. It is guaranteed that:

the string consists only of digits, square brackets and lowercase English letters;
the square brackets form a regular bracket sequence;
all digits that appear in the string represent the number of times the content in the brackets that follow them repeats, i.e. k in the description above;
there are at most 20 pairs of square brackets in the given string.
Guaranteed constraints:
0 ≤ s.length ≤ 80.

[output] string
'''

# 정규표현식으로 풀어도 되지만 문제의 요구는 아마도 스택이나 재귀를 사용하는 것이리라.
def solution_my(s):
    if s == "":
        return ""
    stack_k = []
    stack_s = []
    for i in range(len(s)):
        if s[i].isdigit():
            if i > 0 and s[i-1].isdigit():
                stack_k[-1] = int(str(stack_k[-1]) + s[i])
            else:
                stack_k.append(int(s[i])) # k는 1자리라고 가정
                stack_s.append("")
        elif s[i] == "[":
            pass
        elif s[i] == "]":
            k = stack_k.pop()
            ss = stack_s.pop()
            if stack_s:
                stack_s[-1] += k * ss
            else:
                stack_s.append(k * ss)
        else:
            if stack_s:
                stack_s[-1] += s[i]
            else:
                stack_s.append(s[i])
    return stack_s[0]

# 다른 사람의 더 깔끔한 풀이를 참고했다.
def solution(s):
    stack = [["", 1]]
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        elif c == "[":
            stack.append(["", int(num)])
            num = ""
        elif c == "]":
            ss, k = stack.pop()
            stack[-1][0] += ss * k
        else:
            stack[-1][0] += c
    return stack[-1][0]

print(solution(s = "4[ab]")) # "abababab"
print(solution(s = "2[b3[a]]")) # "baaabaaa"
print(solution(s = "z1[y]zzz2[abc]")) # "zyzzzabcabc"
print(solution(s = "100[codesignal]")) # codesignal * 100