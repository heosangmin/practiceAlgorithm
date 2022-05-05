'''
카드를 뽑는 룰은 다음과 같다.
1. 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

??? 이게 무슨 말인지.
각 행에서 min값을 구하고, 그 값들 중에서 max를 구하면 된다는 소리로 보인다.
'''

def solution_my(nm:str, card:str) -> int:
    n,m = map(int, nm.split())
    card = [r.split() for r in card.split("\n")]
    return max([min(r) for r in card])


nm = "3 3"
card = '''3 1 2
4 1 4
2 2 2'''
print(solution_my(nm, card)) # 2

nm = "2 4"
card = '''7 3 1 8
3 3 3 4'''
print(solution_my(nm, card)) # 3

'''
# input()을 이용해야 하는 경우
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input.split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
'''
