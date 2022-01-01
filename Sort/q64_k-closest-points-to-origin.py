'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
1 <= k <= points.length <= 10^4
-10^4 < xi, yi < 10^4
'''

from typing import List
import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []        
        for point in points:
            # 유클리드 거리(Euclidean Distance)를 구하는 수식은 sqrt((x1-x2)^2 + (y1-y2)^2)이만
            # 여기서는 크기 비교만 하면 되므로 sqrt 연산을 생략할 수도 있다.
            #dist = math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2)
            dist = (0 - point[0]) ** 2 + (0 - point[1]) ** 2
            heapq.heappush(heap, [dist, point])

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

points1, k1 = [[1,3],[-2,2]], 1
points2, k2 = [[3,3],[5,-1],[-2,4]], 2

s = Solution()

print(s.kClosest(points1, k1))
print(s.kClosest(points2, k2))