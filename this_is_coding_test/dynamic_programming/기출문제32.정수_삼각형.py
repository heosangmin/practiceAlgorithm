'''
2022/05/26

https://www.acmicpc.net/problem/1932

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
-> 30
'''

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))