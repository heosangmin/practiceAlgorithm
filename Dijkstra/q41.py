'''
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 104
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst
'''

# 2021-12-12, 리트 코드에서 실행 시간 초과 에러로 풀리지 않음.

from typing import List
import collections, heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        Q = [(0, src, 0)] # price, node, stops

        while Q:
            price, node, stops = heapq.heappop(Q)

            if node == dst:
                return price
            
            if stops <= k:
                stops += 1
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, stops))

        return -1

n1 = 3
flights1 = [[0,1,100],[1,2,100],[0,2,500]]
src1 = 0
dst1 = 2
k1 = 1

n2 = 3
flights2 = [[0,1,100],[1,2,100],[0,2,500]]
src2 = 0
dst2 = 2
k2 = 0

s = Solution()

print(s.findCheapestPrice(n1, flights1, src1, dst1, k1))
print(s.findCheapestPrice(n2, flights2, src2, dst2, k2))