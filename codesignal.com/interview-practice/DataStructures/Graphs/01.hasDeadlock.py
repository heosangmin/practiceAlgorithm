'''
2022/06/14

https://app.codesignal.com/interview-practice/task/ZTqKqNwK6ZL6GDpJ5

In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

Example

For connections = [[1], [2], [3, 4], [4], [0]], the output should be
solution(connections) = true.


This graph contains a cycle.

For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
solution(connections) = false.


This graph doesn't contain a directed cycle (there are two paths from 0 to 3, but no paths from 3 back to 0).
'''

from collections import deque
def solution(connections):
    n = len(connections)

    def bfs(start):
        visited = [False] * n
        q = deque([start])
        visited[start] = True
        while q:
            node = q.popleft()
            for next in connections[node]:
                if next == start:
                    return True
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
        return False
    
    for i in range(len(connections)):
        if bfs(i):
            return True
    return False


connections = [[1], [2], [3, 4], [4], [0]]
print(solution(connections)) # True

connections = [[1, 2, 3], [2, 3], [3], []]
print(solution(connections)) # False

connections = [[1,6],  [2],  [3],  [4],  [5],  [6],  [3]]
print(solution(connections)) # True