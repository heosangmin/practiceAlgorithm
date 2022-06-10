'''
2022/06/10

https://app.codesignal.com/interview-practice/task/BG94ZFECSNo6Kv7XW


Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example

For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
solution(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
solution(nums, k) = 99.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-105 ≤ nums[i] ≤ 105.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ nums.length.

[output] integer
'''

# 주어진 배열에서 k번째 큰 요소를 출력해야 한다.
# 문제에서 바라는 것은 '힙'을 쓰든지 해서 효율적으로 찾는 것일까.
# 풀이를 보니 힙을 직접 구현하는 경우가 많았다.

import heapq
def solution(nums, k):
    q = []
    for num in nums:
        heapq.heappush(q, -num)
    for _ in range(k-1):
        heapq.heappop(q)
    return -heapq.heappop(q)

print(solution(nums = [7, 6, 5, 4, 3, 2, 1], k = 2))
print(solution(nums = [99, 99], k = 1))