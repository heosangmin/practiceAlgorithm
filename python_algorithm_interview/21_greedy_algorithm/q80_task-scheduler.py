'''
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''
from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        좌절을 안겨주는 문제다.
        '''
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break
            
            result += n - sub_count + 1

        return result


s = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print(tasks, n, s.leastInterval(tasks, n))

tasks = ["A","A","A","B","B","B"]
n = 0
print(tasks, n, s.leastInterval(tasks, n))

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(tasks, n, s.leastInterval(tasks, n))