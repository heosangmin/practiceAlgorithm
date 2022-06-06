'''
2022/06/06

https://app.codesignal.com/interview-practice/task/njfXsvjRthFKmMwLC

Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
solution(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
solution(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

Guaranteed constraints:
0 ≤ nums.length ≤ 55000,
-231 - 1 ≤ nums[i] ≤ 231 - 1.

[input] integer k

Guaranteed constraints:
0 ≤ k ≤ 35000.

[output] boolean
'''

def solution(nums, k):
    m = {}
    for i in range(len(nums)):
        if nums[i] not in m:
            m[nums[i]] = [i]
        else:
            m[nums[i]].append(i)
    
    for v in m.values():
        if len(v) > 1:
            for i in range(len(v)-1):
                for j in range(i+1, len(v)):
                    if abs(v[i] - v[j]) <= k:
                        return True
    return False


print(solution(nums = [0, 1, 2, 3, 5, 2], k = 3))
print(solution(nums = [0, 1, 2, 3, 5, 2], k = 2))
print(solution(nums = [1, 0, 1, 1], k = 1)) # True