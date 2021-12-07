'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
'''

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        path = []
        dic = defaultdict(list)

        tickets.sort(key=lambda x:x[0])

        for a,b in tickets:
            if not a in dic:
                dic[a] = []
            dic[a].append(b)

        for a in dic:
            dic[a].sort()

        def dfs(dest: str):
            while dic[dest]:
                dfs(dic[dest].pop(0))
            path.append(dest)

        dfs("JFK")

        return path[::-1]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        # 그래프를 뒤집어서 구성
        for a,b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
        
        dfs("JFK")

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

s = Solution()
tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

print(s.findItinerary1(tickets1))
print(s.findItinerary1(tickets2))
print(s.findItinerary1(tickets3))

print(s.findItinerary2(tickets1))
print(s.findItinerary2(tickets2))
print(s.findItinerary2(tickets3))