'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
'''
import collections
class Solution:
    '''
    피보나치 수열. 살면서 잊을만 하면 나타나는 그 녀석. 하지만 매번 새로운 그 녀석.
    책에 나온 정의는 다음과 같다.
    "수학에서 피보나치 수는 Fn으로 표기하며, 피보나치 수열이라는 수열을 형성한다.
    각 수는 0과 1에서부터 시작된 앞 두 숫자의 합이 된다."
    즉 F0 = 0, F1 = 1이며 n > 1에 대해 Fn = Fn-1 + Fn-2이 된다.
    '''

    def fib_bf(self, n: int) -> int:
        '''
        피보나치 수열의 수도코드 대로 구현함.
        하지만 실행 속도는 좋지 못하다.
        '''
        if n <= 1:
            return n
        return self.fib_bf(n - 1) + self.fib_bf(n - 2)

    dp = collections.defaultdict(int)
    def fib_memoization(self, n: int) -> int:
        '''
        하향식(메모이제이션) 풀이
        수도코드를 봤을 때는 이해가 잘 안 갔었는데 dp를 저장 공간으로 쓰는 것을 보니까 알겠다.
        이미 계산 했던 수열은 저장했으므로 다시 계산할 필요가 없어 효율이 좋아진다.
        리트코드에서 bf가 823ms였는데 이 방식은 32ms가 나왔다.
        '''
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib_memoization(n - 1) + self.fib_memoization(n -2)
        return self.dp[n]

    def fib_tabulation(self, n: int) -> int:
        '''
        상향식(타뷸레이션) 풀이
        하향식에서도 그랬지만 "중복된 하위 문제들"을 저장해 놓는 과정이 중요하다는 것일까.
        '''
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]

    def fib_simple(self, n: int) -> int:
        '''
        위에서는 딕셔너리를 이용해서 하위 문제의 답을 저장해 뒀지만
        변수 두 개만을 사용해서 풀 수도 있다. 즉, 공간 복잡도가 O(n)에서 O(1)로 줄어든다.
        '''
        x, y = 0, 1
        for _ in range(0, n):
            x, y = y, x + y
        return x

s = Solution()

n = 2
# print(n, s.fib_bf(n))
# print(n, s.fib_memoization(n))
# print(n, s.fib_tabulation(n))
print(n, s.fib_simple(n))

n = 3
# print(n, s.fib_bf(n))
# print(n, s.fib_memoization(n))
# print(n, s.fib_tabulation(n))
print(n, s.fib_simple(n))

n = 4
# print(n, s.fib_bf(n))
# print(n, s.fib_memoization(n))
# print(n, s.fib_tabulation(n))
print(n, s.fib_simple(n))