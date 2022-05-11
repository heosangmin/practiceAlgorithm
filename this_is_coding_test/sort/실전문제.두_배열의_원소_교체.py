'''
2022/05/09

배열 A와 B가 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다. 사용자는 최대 K번의 바꿔치기 연산을 수행할 수 있다. 최종 목표는 배열 A의 모든 원소의 값이 최대가 되도록 하는 것이다.

input)
5 3
1 2 5 4 3
5 5 6 6 5

output)
26
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때 더이상의 비교는 의미가 없으므로 끝
        break

print(sum(a))
