'''
2022/05/06

Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
'''

import re
def solution(time):
    # return bool(re.match("(^[01][0-9]:[0-5][0-9]$)|(^2[0-3]:[0-5][0-9]$)", time))
    time = list(map(int, time.split(":")))
    return 0 <= time[0] <= 23 and 0 <= time[1] <= 59

'''
정규표현식으로 정의할 수 있겠지만 막상 해보니 의외로 간단하지 않다.
24일 때 분은 0일 뿐이니까 표현식이 길어진다. <- wrong
00:00~23:59가 유효한 데이터였다.
'''

print(solution(time = "13:58")) # t
print(solution(time = "25:51")) # f
print(solution(time = "02:76")) # f
print(solution(time = "24:09")) # f
print(solution(time = "24:00")) # f
