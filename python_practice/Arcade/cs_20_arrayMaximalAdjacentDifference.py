'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
'''

# import sys
# def solution(inputArray):
#     result = -sys.maxsize
#     for i in range(0, len(inputArray)-1):
#         result = max(result, abs(inputArray[i] - inputArray[i+1]))
#     return result

def solution(inputArray):
    diffs = [abs(inputArray[i]-inputArray[i+1]) for i in range(0,len(inputArray)-1)]
    return max(diffs)

print(solution([2, 4, 1, 0])) # 3