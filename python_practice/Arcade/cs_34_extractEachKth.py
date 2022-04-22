'''
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
'''
def solution(inputArray, k):
    return [x for i,x in enumerate(inputArray) if (i+1) % k != 0]

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)) # [1, 2, 4, 5, 7, 8, 10]

'''
다음처럼 직접 지우는 방법도 있음.
del inputArray[k-1::k]
'''