'''
2022/05/09

각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

input)
2
홍길동 95
이순신 77

output)
이순신 홍길동
'''

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end= ' ')

