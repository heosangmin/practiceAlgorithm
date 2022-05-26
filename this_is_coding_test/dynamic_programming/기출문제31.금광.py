'''
2022/05/26

n*m 크기의 금광이 있다. 금광은 1*1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작하나. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라.

1 3 3 2
2 1 4 1
0 6 4 7

가장 왼쪽 위의 위치를 (1,1), 가장 오른쪽 아래의 위치를(n,m)이라고 할때, 위 예시에서는 (2,1) -> (3,2) -> (3,3) -> (3,4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최대값이다.

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    temp_data = list(map(int, input().split()))
    
    dp = []
    for i in range(0, n*m, m):
        dp.append(temp_data[i:i+m])
    
    # 다이나믹 프로그래밍 시작
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # dp 테이블 갱신
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)