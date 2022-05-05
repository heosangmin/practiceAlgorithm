'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
'''

def solution(n):
    # m = 0
    # s = str(n)
    # for i in range(len(s)):
    #     m = max(int(s[0:i] + s[i+1:]), m)
    # return m

    n = str(n)
    return max([int(n[:i] + n[i+1:]) for i in range(len(n))])


print(solution(n = 152)) # 52
print(solution(n = 1001)) # 101


'''
무식한 방법이라면 숫자 하나씩 지워가며 최대값인지 확인하는 것일까.
하지만 분명 더 좋은 방법이 있을 것이다.
'''