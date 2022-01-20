def fractional_kanpsack(cargo):
    capacity = 15
    pack = []
    # 단가 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1])) # c[0] / c[1] = 단가
    pack.sort(reverse=True)
    print(pack)
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0: # 짐을 하나 통째로 넣을 수 있는 공간이 남아 있음.
            capacity -= p[2]
            total_value += p[1]
        else: # 짐을 하나 통째로 넣을 수 없기 때문에 쪼갬(fraction).
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    return total_value

cargo = [
    (4,12), # (가격, 무게)
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]
print("result: ", fractional_kanpsack(cargo))