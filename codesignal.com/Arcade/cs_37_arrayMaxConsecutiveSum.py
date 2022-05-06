'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
'''
# import sys
# def solution(inputArray, k):
#     maxValue = -sys.maxsize
#     for i in range(0, len(inputArray)-k+1):
#         maxValue = max(maxValue, sum(inputArray[i:i+k]))
#     return maxValue

'''
위 풀이는 타임아웃이 발생하는데 다른 사람 풀이를 보니 역시 sum()이 시간을 잡아먹는 것 같다.
'''

def solution(inputArray, k):
    m = c = sum(inputArray[:k])
    for i in range(len(inputArray)-k):
        print(i)
        c = c + inputArray[i+k] - inputArray[i]
        m = max(c, m)
    return m

print(solution([2, 3, 5, 1, 6], 2)) # 8

