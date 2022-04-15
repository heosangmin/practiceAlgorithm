'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
'''

# def solution(n):
#     for x in str(n):
#         if int(x) % 2 != 0:
#             return False
#     return True

# 갑자기 왜 난이도가 급락한거지?
# 동시에 다른 언어에서라면 어떻게 풀어야할지 궁금해지기도 한다.
# 파이썬이야 문자열 다루기가 상대적으로 편해서 이런 풀이 방식이 바로 떠오르지만
# 아닌 경우에는 산수로 푸는 편이 빠를 지도 모른다.

def solution(n):
    while n > 0:
        if (n % 10) % 2 != 0:
            return False
        n = n // 10
    return True

# return all([int(i)%2==0 for i in str(n)])
# 이런 방법도 있다.

print(solution(248622)) # True
print(solution(642386)) # False
