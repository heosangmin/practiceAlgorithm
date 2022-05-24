'''
2022/05/24

https://programmers.co.kr/learn/courses/30/lessons/42889

N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]
'''


def solution(N, stages):
    result = []
    # stages.sort()
    players = [0] * (N+2)

    for stage in range(1, N+2):
        players[stage] = stages.count(stage)

    print(players)

    for stage in range(1, N+1):
        reached_players = sum(players[stage:])
        uncleared_players = players[stage]
        print(stage, reached_players, uncleared_players)
        if reached_players == 0:
            result.append((0, stage))
        else:
            result.append((uncleared_players/reached_players, stage))

    result.sort(key=lambda x:(-x[0], x[1]))

    return [x[1] for x in result]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4,1,2,3]
