'''
2022/05/07

8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

input)
a1

output)
2
'''

def solution_my(k):
    r = 0
    k = ( ord(k[0])-ord('a'), int(k[1])-1 )
    direction = [(1,2), (2,1), (2,-1), (1,-2), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
    for d in direction:
        if 0 <= k[0] + d[0] <= 8 and 0 <= k[1] + d[1] <= 8:
            r += 1
    return r

print(solution_my("a1"))
print(solution_my("d3"))