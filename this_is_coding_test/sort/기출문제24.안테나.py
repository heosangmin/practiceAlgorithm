'''
2022/05/24

4
5 1 7 9
-> 5
'''

n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[(n-1)//2])