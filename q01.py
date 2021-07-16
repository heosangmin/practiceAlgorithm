'''
q01. 유효한 팰린드롬

"A man, a plan, a canal: Panama" -> true
"race a car" -> false

'''

from collections import deque
from typing import Deque
import time
import re

# 1
# pop()을 이용해 배열 첫 요소와 마지막 요소를 비교하는 방법
# pop(0)이 O(n) 이므로 n번 반복시 O(n^2)의 복잡도를 가진다
def ans1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# 2
# deque 이용
# dequq의 popleft는 O(1)이기 때문에 n번 반복시 O(n)의 복잡도를 가짐
def ans2(s: str) -> bool:
    # 자료형을 데크로 변경
    strs: Deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True


# 3
# 슬라이싱
def ans3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # s를 뒤집는다


start = time.time()
result = ans1(s = "A man, a plan, a canal: Panama")
done = time.time()
print(result, done-start)


start = time.time()
result = ans2(s = "A man, a plan, a canal: Panama")
done = time.time()
print(result, done-start)

start = time.time()
result = ans3(s = "A man, a plan, a canal: Panama")
done = time.time()
print(result, done-start)