'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어졌을 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

2 <= N <= 100000
2 <= K <= 100000
'''

def solution_my(input:str) -> int:
    n,k = map(int, input.split())
    c = 0

    while n != 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        
        c += 1

        if n < k:
            c += n - 1
            n -= n - 1

    return c

input = "25 5" # 2
print(solution_my(input))
input = "25 3" # 6
print(solution_my(input))

'''
N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로 한 번에 빼는  방식으로 작성할 수 있다.
'''

def solution(input:str) -> int:
    n,k = map(int, input.split())
    result = 0

    while True:
        # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        
        # K로 나누기
        result += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1)
    return result

input = "25 5" # 2
print(solution_my(input))
input = "25 3" # 6
print(solution_my(input))