'''
2022/05/24

https://www.acmicpc.net/problem/10825

12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

->
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().split()))

data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for v in data:
    print(v[0])
