'''
2022/05/11

가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 이 얇은 바닥을 1*2의 덮개, 2*1의 덮개, 2*2의 덮개를 이용해 채우고자 한다.

이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

cond)
1 <= n <= 1000

input)
3

output) 방법의 수를 796,796으로 나눈 나머지를 출력한다.(결괏값이 매우 커질 수 있으므로)
5

왼쪽부터 차례대로 바닥을 채운다고 생각하면 어렵지 않게 점화식을 세울 수 있다.
1. 왼쪽부터 i-1까지 이미 덮개가 채워져 있으면 2*1의 덮개를 채우는 하나의 경우밖에 존재하지 않는다.
2. 왼쪽부터 i-2까지 이미 덮개가 채워져 있으면 1*2 덮개 2개 혹은 2*2 덮개 하나를 채우는 경우 2가지 존재한다.(?????? 3개 아니고???)

왼쪽부터 n-2 미만의 갈이에 대해서는 고려할 필요가 없다. 왜냐하면 사용할 수 있는 덮개의 형태가 최대 2*2의 정사각형 형태이기 때문이다. 다시 말해 바닥을 채울 수 있는 형태는 뒤에서 언급한 경우밖에 없다. 따라서 다음과 같이 점화식을 세울 수 있다.

a[i] = a[i-1] + a[i-2] * 2

왼쪽부터 n-2까지 덮개로 이미 채워져 있는 경우 덮개를 채우는 방법은 2가지 경우가 있다. 이 두 방법은 서로 다른 것이므로, 결과적으로는 a[i]는 a[i-1] + a[i-2] + a[i-2]가 된다. 따라서 이를 간략히 a[i] = a[i-1] + a[i-2] * 2로 표현할 수 있다.
'''

n = 3

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])
