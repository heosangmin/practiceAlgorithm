'''
2022/05/19

치킨 배달
https://www.acmicpc.net/problem/15686

'''

# 결국 책의 풀이와 방식은 동일했다.
# 하지만 입력 조건을 보고 모든 조건을 테스트하는 방식으로 해도 될지 결정하는 과정이 필요하다.
# nCm 이 10만을 넘기지 않는다는 것을 먼저 파악하고, 지금과 같은 방식으로 하자고 결정하는 것이 좋았을 것이다.

import itertools

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

def get_cd(homes, bhcs):
    cd = []
    for home in homes:
        min_cd = 2501
        for bhc in bhcs:
            min_cd = min(min_cd, abs(home[0] - bhc[0]) + abs(home[1] - bhc[1]))
        cd.append(min_cd)
    return sum(cd)

def solution(n, m, city):
    
    homes = []
    bhcs = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                homes.append((i,j))
            elif city[i][j] == 2:
                bhcs.append((i,j))

    possible_bhcs = list(itertools.combinations(bhcs, m))
    min_cd = 2501
    for pbhcs in possible_bhcs:
        min_cd = min(min_cd, get_cd(homes, pbhcs))
    
    return min_cd

print(solution(n, m, city)) # 5