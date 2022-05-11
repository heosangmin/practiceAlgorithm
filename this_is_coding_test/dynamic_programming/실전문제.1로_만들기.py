'''
2022/05/11

정수 x가 주어졌을 때 x가 사용할 수 있는 연산은 다음과 같이 4가지이다.

1. x가 5로 나누어떨어지면, 5로 나눈다.
2. x가 3으로 나누어떨어지면, 3으로 나눈다.
3. x가 2로 나누어떨어지면, 2로 나눈다.
4. x에서 1을 뺀다.

x가 주어졌을 때, 연산 4개를 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

cond)
1 <= x <= 30000

input)
26

output)
3

'''

def solution(x):
    d = [0] * 30001
    
    for i in range(2, x+1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i - 1] + 1

        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        
        # 현재의 수가 3로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)

        # 현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    
    return d[x]

x = 26
print("result:", solution(x))