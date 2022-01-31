'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''
import collections
class Solution:
    '''
    이게 도대체 무슨 말인가 싶었다.
    한 번에 1계단 또는 2계단을 올라갈 수 있다.
    n개의 계단에 오르기 위한 경로의 수는?

    피보나치 수열과 비슷하다고 책에서 봤을 땐 지난 세월이 떠올랐다.
    중고등학교 수학 시간에 공식을 외운들 문제를 봐도 풀이 방법이 떠오르지 않는 순간들 말이다.
    항상 응용력 응용력. 봐도 모르겠고 내가 바보 같고 수학 머리는 절대 아닌 것 같은 자괴감들.
    뭐가 문제였을까. 그냥 계속해서 시간을 들이면 언젠간 해결 되는 고민이었을까.

    암튼.
    n = 1일 경우, 1경로
        - 1
    n = 2일 경우, 2경로
        - 1 + 1
        - 2
    n = 3일 경우, 3경로
        - 1 + 1 + 1
        - 1 + 2
        - 2 + 1
    n = 4일 경우, 5경로
        - 1 + 1 + 1 + 1
        - 1 + 1 + 2
        - 1 + 2 + 1
        - 2 + 1 + 1
        - 2 + 2

    위의 실제 값을 보면 피보나치 수열의 그것과 같다. n > 2일떄, f(n) = f(n-1) + f(n-2)
    '''
    def climbStairs_bf(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs_bf(n - 1) + self.climbStairs_bf(n - 2)


    dp = collections.defaultdict(int)
    def climbStairs_memoization(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.climbStairs_memoization(n - 1) + self.climbStairs_memoization(n - 2)

        return self.dp[n]

    def climbStairs_tabulation(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]

s = Solution()

n = 2
# print(n, s.climbStairs_bf(n))
# print(n, s.climbStairs_memoization(n))
print(n, s.climbStairs_tabulation(n))

n = 3
# print(n, s.climbStairs_bf(n))
# print(n, s.climbStairs_memoization(n))
print(n, s.climbStairs_tabulation(n))

n = 10
# print(n, s.climbStairs_bf(n))
# print(n, s.climbStairs_memoization(n))
print(n, s.climbStairs_tabulation(n))