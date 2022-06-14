'''
2022/06/14

https://app.codesignal.com/interview-practice/task/qmKLsQcqeEBckLx2q

Note: Try to solve this task in O(n2) time, where n is a number of vertices, since this is what you'll be asked to do during an interview.

Sue is a network administrator who consults for companies that have massive Local Area Networks (LANs). The computers are connected together with network cables, and Sue has been brought in to evaluate the company’s network. The networks are huge, and she wants to ensure that no single network cable failure can disconnect the network. Any cable that fails that leaves the network in two or more disconnected pieces is called a single point of failure.

She labels the different network devices from 0 to n - 1. She keeps an n × n matrix connections, where connections[i][j] = 1 if there is a network cable directly connecting devices i and j, and 0 otherwise. Write a function that takes the matrix of connections, and returns the number of cables that are a single point of failure.

Example

For connections = [[0, 1], [1, 0]], the output should be
solution(connections) = 1.
A failure of the cable that connects devices 0 and 1 would leave the network disconnected.



For connections = [[0, 1, 1], [1, 0, 1], [1, 1, 0]], the output should be
solution(connections) = 0.
No failure of a single network cable would result in the network being disconnected.



For connections = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]], the output should be
solution(connections) = 3.
The three cables that are single points of failure are connected with device 3:



For connections = [[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], the output should be
solution(connections) = 4.
In this topology, every cable is a single point of failure:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer connections

Representations of connections between computers. connections[i][j] = 1 if there is a network cable directly connecting devices i and j, and 0 otherwise. It is guaranteed that the original network is connected.

Guaranteed constraints:
1 ≤ connections.length ≤ 300,
connections[i].length = connections.length,
connections[i][i] = 0,
 0 ≤ connections[i][j] ≤ 1,
connections[i][j] = connections[j][i].

[output] integer

The number of cables in the network that are a single point of failure.
'''

# thanks user [navravi]
# 그래프 내에서 단일 실패 지점을 찾는 문제인데
# 기본 아이디어는 노드간에 우회로가 없는 간선 수를 찾는 것이다.
# 위 유저의 방식으로는, 각 노드에 대해서 타겟 노드로의 간선이 있다면 일시적으로 제외시킨 다음
# 경로 탐색으로 도달할 수 있다면 단일 실패 지점이 아닌 것으로 판단한다.
def solution(connections):
    n = len(connections)
    result = 0

    def is_reachable(i, j):
        stack = [i]
        visited = set()
        while stack:
            k = stack.pop()
            if k == j: # i에서 j로의 우회로가 존재
                return True
            visited.add(k)
            for v in range(n):
                if connections[k][v] == 1 and v not in visited:
                    stack.append(v)
        return False


    for i in range(n):
        for j in range(i):
            if connections[i][j] == 0:
                continue
            # i에서 j로 간선이 존재한다면
            # 일시적으로 간선을 지우고
            connections[i][j] = 0
            connections[j][i] = 0
            # i에서 j로의 우회로가 없다면 카운트 + 1
            if not is_reachable(i, j):
                result += 1
            # 지웠던 간선을 복구
            connections[i][j] = 1
            connections[j][i] = 1
    
    return result

connections = [[0, 1], [1, 0]]
print(solution(connections)) # 1
connections = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print(solution(connections)) # 0
connections = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
print(solution(connections)) # 3
connections = [[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
print(solution(connections)) # 4
