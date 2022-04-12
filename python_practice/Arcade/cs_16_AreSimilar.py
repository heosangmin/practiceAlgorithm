'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
'''


# def solution(a, b):
#     if sorted(a) != sorted(b):
#         return False
#     diffCount = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             diffCount += 1
#         if diffCount > 2:
#             return False
#     return True

def solution(a, b):
    return sorted(a) == sorted(b) and sum([A!=B for A,B in zip(a,b)]) <= 2

# 문제의 상황을 복잡하게 생각한 것이 고전한 이유임.
# 두 요소만 스왑해서 같은 리스트가 되는 것이 참이라면
# 그 두 요소 외에 다른 요소들은 각각의 리스트에서 인덱스가 같음. 
# 즉, 요소를 스왑한다고 해서 요소들이 한 칸씩 뒤로 밀리지 않는다고 생각했어야 했음.

print(solution([1, 2, 3], [2, 1, 3]))
print(solution([1, 2, 2], [2, 1, 1]))
print(solution([4, 6, 3], [3, 4, 6])) # false
print(solution([], []))
