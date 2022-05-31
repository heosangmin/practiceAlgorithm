'''
소수 판별 함수
에라토스테네스의 체

1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다).
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

'''

import math

n = 1000 # 2부터 1000까지의 모든 수에 대해 소수 판별
array = [True for _ in range(n+1)] # 처음에는 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
