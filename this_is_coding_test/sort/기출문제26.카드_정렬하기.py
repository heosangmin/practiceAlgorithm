'''
2022/05/24

https://www.acmicpc.net/problem/1715

3
10
20
40
-> 100
'''
import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

total = 0
while q:
    card1 = heapq.heappop(q)
    if len(q) > 0:
        card2 = heapq.heappop(q)
        total += card1 + card2
        heapq.heappush(q, card1 + card2)
    else:
        break

print(total)
