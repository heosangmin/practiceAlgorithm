'''
2022/05/06

여행가 A는 N*N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1*1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다. 여행가는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.

정사각형 공간을 벗어나는 움직임은 무시된다.

계획서가 주어졌을 때 여행가가 최종적으로 도착하는 지점의 좌표를 출력하는 프로그램을 작성하시오.

ex)
5
R R R U D D

ans)
3 4
'''

def solution_my(n: int, p: str) -> str:
    t = [1,1]
    p = p.split()

    for d in p:
        if d == "L" and t[1] > 1:
            t[1] -= 1
        if d == "R" and t[1] < n:
            t[1] += 1
        if d == "U" and t[0] > 1:
            t[0] -= 1
        if d == "D" and t[0] < n:
            t[0] += 1

    return " ".join(map(str, t))
        

print(solution_my(n = 5, p = "R R R U D D"))


def solution_book():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ["L", "R", "U", "D"]

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    
    print(x, y)