'''
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
'''

# def solution(inputString):
#     d = {}
    
#     for i in range(26):
#         d[chr(ord('a') + i)] = 0

#     for c in inputString:
#         d[c] += 1
    
#     for i in range(len(list(d.keys()))-1):
#         if d[list(d.keys())[i]] < d[list(d.keys())[i+1]]:
#             return False

#     return True
import string
def solution(inputString):
    r = [inputString.count(c) for c in string.ascii_lowercase]
    return r[::-1] == sorted(r)

print(solution(inputString = "bbbaacdafe"))
print(solution(inputString = "aabbb"))
print(solution(inputString = "bbc"))

'''
문제를 다시 읽어보니 그다지 단순한 케이스는 아니었다.
모든 알파벳이 존재하고, 앞의 알파벳의 수가 뒤 알파벳 수보다 많은 경우를 말하는 것이다.
한 번의 루프로 끝내는 건 가능할까?
무식하게 풀자면 딕셔너리를 쓰면 되긴 하다. 카운터랄지.

아마 리스트 컴프리헨션과 같은 기능으로 각 알파벳의 수의 리스트로 만들어 줄 수도 있을 것이다.
그러면 배열을 탐색하면서 앞뒤의 수를 비교하는 것으로 결론을 낼 수 있겠지.

위와 같은 무식한 방법으로 풀이는 통과했지만 다른 사람의 그것을 보니 역시나였다.
우선 알파벳을 하나하나 딕셔너리에 입력했던 것을 대신하는 것으로
string 모듈에는 string.ascii_lowercase와 같은 기본적인 데이터가 정의되어 있었다.
1.그걸로 inputString에 각 알파벳의 수를 count()로 뽑아서 리스트 r로 만든다.
2. r의 reverse된 리스트와 r의 정렬된 리스트가 같다면(알파벳 순서대로 개수가 적어지는 조건) True
'''