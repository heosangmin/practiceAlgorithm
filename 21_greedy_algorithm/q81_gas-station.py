'''
134. Gas Station
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:
gas.length == n
cost.length == n
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
'''
from typing import List

class Solution:
    def canCompleteCircuit_bf(self, gas: List[int], cost: List[int]) -> int:
        '''
        O(n^2)이라 효율적이지 못하다.
        게다가 난 이 마저도 내 힘으로 풀지 못했다.
        인덱스는 늘 헷갈린다.
        '''
        length = len(gas)
        for start in range(length):
            tank = 0
            for i in range(start, length + start):
                index = i % length
                can_travel = True
                if gas[index] + tank < cost[index]:
                    can_travel = False
                    break
                else:
                    tank += gas[index] - cost[index]
            
            if can_travel:
                return start
                
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        1. 전체 gas가 전체 cost보다 작다면 모든 인덱스를 다 탐색할 수 없다는 뜻이 된다.
        2. 1의 경우를 제외하고는 전체를 방문할 수 있는 시작점이 반드시 하나 존재한다는 뜻이 된다.
           그래서 모든 인덱스에서 각각 다음 지점으로 갈 수 있는 조건인지 체크한다.
        '''
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if fuel + gas[i] < cost[i]: # 현재 인덱스가 조건을 만족하지 않는다면
                start = i + 1 # 다음 인덱스가 답이라고 가정하고
                fuel = 0 # 다음 인덱스를 출발점으로 만든다.
            else:
                fuel += gas[i] - cost[i]
        return start

s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# print(gas, cost, s.canCompleteCircuit_bf(gas, cost))
print(gas, cost, s.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
# print(gas, cost, s.canCompleteCircuit_bf(gas, cost))
print(gas, cost, s.canCompleteCircuit(gas, cost))

gas = [4,5,3,1,4]
cost = [5,4,3,4,2]
# print(gas, cost, s.canCompleteCircuit_bf(gas, cost))
print(gas, cost, s.canCompleteCircuit(gas, cost))