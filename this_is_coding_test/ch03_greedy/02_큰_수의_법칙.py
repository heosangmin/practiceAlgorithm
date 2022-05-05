'''
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 "저자의" 큰 수의 법칙에 따른 결과를 출력하시오.

입력 예시
5 8 3
2 4 5 4 6

출력 예시
46

'''

def solution(input:str, data:str) -> int:
    n, m, k = map(int, input.split())
    data: list(int) = list(map(int, data.split()))
    
    data.sort()
    m1:int = data[-1]
    m2:int = data[-2]
    r:int = 0

    while True:
        for _ in range(k):
            if m == 0:
                break
            r += m1
            m -= 1
        if m == 0:
            break
        r += m2
        m -= 1
    
    return r

input = "5 8 3"
data = "2 4 5 4 6"
print(solution(input, data))

'''
이 문제는 M이 10000 이하이므로 이 방식으로도 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다. 간단한 수학적 아이디어를 이용해 더 효율적으로 문제를 해결해보자.

이 문제를 풀려면 가장 먼저 "반복되는 수열에 대해 파악"해야 한다. 가장 큰 수와 두 번째로 큰 수가 더해질 떄는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다. 위의 예시에서는 수열 {6,6,6,5}가 반복된다. 그렇다면 반복되는 수열의 길이는 어떻게 될까? 바로 (K+1)로 위의 예시에서는 4가 된다. 따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 된다. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.

이때 M이 (K+1)로 나누어떨어지지 않는 경우도 고려해야 한다. 그럴 때는 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려해주어야 한다. 즉, '가장 큰 수가 더해지는 횟수'는 다음과 같다.

int(M / (K + 1)) * K + M % (K + 1)

결과적으로 위의 식을 이용하여 가장 큰 수가 더해지는 횟수를 구한 다음, 이를 이용해 두 번째로 큰 수가 더해지는 횟수까지 구할 수 있는 것이다.
'''

def solution2(input:str, data:str) -> int:
    n, m, k = map(int, input.split())
    data: list(int) = list(map(int, data.split()))

    data.sort()
    m1:int = data[-1]
    m2:int = data[-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += (count) * m1 # 가장 큰 수 더하기
    result += (m - count) * m2 # 두 번째로 큰 수 더하기

    return result

input = "5 8 3"
data = "2 4 5 4 6"
print(solution2(input, data))