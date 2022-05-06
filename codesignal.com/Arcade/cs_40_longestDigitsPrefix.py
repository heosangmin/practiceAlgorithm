'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
'''
import re

def solution(inputString):
    digit_list = re.findall("^\d*", inputString)
    return digit_list[0]


print(solution("123aa1")) # "123"
print(solution("the output is 42")) # ""
print(solution("aaaaaaa")) # ""
print(solution("  3) always check for whitespaces")) # ""

'''
정규표현식으로 연속된 숫자의 문자열을 그룹으로 추출해도 좋을 것이고
한 자씩 반복해가며 숫자 문자열을 저장해가는 식으로 비교할 수도 있겠다.
같은 길이의 숫자 문자열들이 존재할 경우 어떻게 처리할 지가 신경 쓰이는 부분이다.

문제를 제대로 이해하지 못했다.
프리픽스(공백 외의 캐릭터)중에서 숫자 부분만 뽑아야하는데
정규표현식으로 시도하다가 시간이 너무 들어서 보류. 아마 다른 사람들의 풀이를 참고해야겠다.

digit_list = re.findall("^\d*", inputString)
return digit_list[0]

로 풀린다고??????

정말 자주 발생하는 일인데
나는 문제를 어렵게 접근하려고 한다.
'''