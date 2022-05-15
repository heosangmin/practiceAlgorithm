'''
2022/05/15

곱하기 혹은 더하기

각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라. 단, +보다 *를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.

input cond)
첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다. (1 <= len(s) <= 20)

output cond)
첫째 줄에 만들어질 수 있는 가장 큰 수를 출력한다.

input)
02984

output)
576

input)
567

output)
210
'''

# 0이나 1이 나오면 더해주고, 나머지는 곱해주면 되는 거 아닌가? -> 맞음
# s = input()
# result = -1
# for i in s:
#     if result == -1:
#         result = int(i)
#         continue
#     if result == 0 or int(i) == 0 or int(i) == 1:
#         result += int(i)
#     else:
#         result *= int(i)
# print(result)

data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print (result)
