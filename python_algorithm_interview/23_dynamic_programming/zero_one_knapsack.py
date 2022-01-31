def zero_one_knapsack(cargo):
    capacity = 15 # 최대 배낭 용량
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0) # 0행, 0열은 0으로 채우고 시작(짐도 없고 배낭 용량도 없음. 즉 0임.)
            elif cargo[i - 1][1] <= c: # i번째 짐의 무게가 현재 배낭 용량(c)에 들어갈 수 있는가
                pack[i].append( # 다음 둘 중에 큰 것을 할당함
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]], # 현재 고려 중인 짐의 값 + 이미 더해진 짐들의 값(c - cargo[i - 1][1]: 배낭(c)에서 현재 고려 중인 짐의 무게(cargo[i - 1][1])를 빼면 이미 더해진 짐들의 값)
                        pack[i - 1][c] # 앞의 행(i-1)에서 이미 구해놓은 값(이미 구해진 중복된 하위 문제)
                    )
                )
            else: # i번째 짐의 무게를 현재 배낭(c)에 넣을 수 없으면
                pack[i].append(pack[i - 1][c]) # 앞의 행(i-1)에서 이미 구해놓은 값(이미 구해진 중복된 하위 문제)을 할당함.
    
    for row in pack:
        print(row)

    return pack[-1][-1]

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]

r = zero_one_knapsack(cargo)
print(r)