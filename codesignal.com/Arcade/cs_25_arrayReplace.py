'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''
# def solution(inputArray, elemToReplace, substitutionElem):
#     result = []
#     for x in inputArray:
#         if x == elemToReplace:
#             result.append(substitutionElem)
#         else:
#             result.append(x)
#     return result

# 분명 한 줄로 해결될텐데 방법을 모르겠다????
# 그런데 이거 함정픽인가? 갑자기 난이도가 급 하락하잖아.

# 풀이후:
# 리스트 컴프리헨션 쓰는 방법을 모르고 있었다.
# 다음과 같이 하면 됨.
def solution(inputArray, elemToReplace, substitutionElem):
    return [x if x != elemToReplace else substitutionElem for x in inputArray]

print(solution([1, 2, 1], 1, 3))
