'''
2022/05/12

1번부터 N번까지의 회사가 있는데 서로 도로를 통해 연결되어 있다.
판매원 A는 1번 회사에 있다.
회사가 서로 연결되어 있다면 이동 시간은 1이다.
판매원 A는 1번 회사에서 출발하여 K번 회사를 방문하고 X번 회사로 가는 것이 목표다. 최소 시간을 구하는 프로그램을 작성하시오.

cond)
1 <= N,M <= 100
첫재 줄에 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.
줄째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M+2번째 줄에는 X과 K가 공백으로 구분되어 차례대로 주어진다.(1 <= K <= 100)

input)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

output)
3

input)
4 2
1 3
2 4
3 4

output)
-1
'''

INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [ [INF] * (n + 1) for _ in range(n + 1) ]

# 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A과 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1을 출력
if distance == INF:
    print("-1")
else:
    print(distance)

