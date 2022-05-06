'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''

def solution(n):
    if n < 10:
        return 0
    return solution(sum([int(x) for x in str(n)])) + 1

print(solution(n = 5))
print(solution(n = 100))
print(solution(n = 91))

'''
재귀를 쓰는 건 늘 헷갈린다. 하지만 결국 깔끔하게 할 수 있다는 것을 잊지말자.
'''