'''
2022/05/27

https://www.acmicpc.net/problem/11404

'''

n = int(input()) # 1 <= n <= 100
m = int(input()) # 1 <= m <= 100,000

# 전체 비용을 INF로 초기화
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]

# 같은 도시로 향하는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

 # 비용 입력받기
for _ in range(m):
    a, b, x = map(int, input().split())
    graph[a][b] = min(graph[a][b], x)

# 플로이드 워셜 알고리즘 수행
# min(graph[a][b], graph[a][k] + graph[k][a])
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print
# for i in range(1, n+1):
#     print(" ".join(list(map(str,graph[i][1:]))))
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없으면 0 출력
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
