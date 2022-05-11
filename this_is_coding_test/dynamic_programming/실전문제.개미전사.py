'''
2022/05/11

leetcode의 q88_house-robber와 같은 문제

cond)
3 <= n <= 100
0 <= k <= 1000

input)
4
1 3 1 5

output)
8
'''

def solution_my(n, array):
    d = [0] * 1001

    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + array[i])
    
    return d[n-1]

print(solution_my(4, [1,3,1,5]))