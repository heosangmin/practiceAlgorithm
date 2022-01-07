'''
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4

Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2^31 - 1
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        자연어 처리에서도 널리 쓰이는 해밍 거리(Hamming Distance)는
        두 정수 또는 두 문자열의 차이를 말한다.
        예를 들어, "karolin"과 "kathrin"의 차이는 3이고 1011101과 1001001의 차이는 2다.
        문자열의 경우 해밍 거리는 다른 자리의 문자 개수가 되며,
        이진수의 경우 다른 위치의 비트 개수가 된다.
        '''
        return bin(x ^ y).count("1")

s = Solution()

x = 1
y = 4
print(x, y, s.hammingDistance(x, y))

x = 3
y = 1
print(x, y, s.hammingDistance(x, y))