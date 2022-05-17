'''
2022/05/17

문자열 재정렬

알파벳 대분자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.

input cond)
하나의 문자열 S가 주어진다. (1 <= len(S) <= 10,000)

input)
K1KA5CB7

output)
ABCKK13

input)
AJKDLSI412K4JSJ9D

output)
ADDIJJJKKLSS20
'''

s = input()

str_list = []
digit_list = []

for c in s:
    if c.isdigit():
        digit_list.append(c)
    else:
        str_list.append(c)
print("".join(sorted(str_list)) + str(sum(map(int,digit_list))))

import re
print("".join(sorted(re.findall("[a-zA-Z]", s))) + str(sum(map(int,re.findall("\d", s)))))