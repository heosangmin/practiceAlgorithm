'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
'''

def solution(inputArray):
    result = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            result += inputArray[i-1] - inputArray[i] + 1
            inputArray[i] += inputArray[i-1] - inputArray[i] + 1
    return result


print(solution([1, 1, 1])) # 3
print(solution([-1000, 0, -2, 0])) # 5
print(solution([2, 1, 10, 1])) # 12
print(solution([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15])) # 13
print(solution([3122, -645, 2616, 13213, -8069])) # 25559
