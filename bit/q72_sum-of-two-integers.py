'''
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
'''

class Solution:
    def getSum1(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF

        a_bin = bin(a & mask)[2:].zfill(32)
        b_bin = bin(b & mask)[2:].zfill(32)

        carry = 0
        result = []

        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
        
            Q1 = A & B
            Q2 = A ^ B
            Q3 = carry & Q2
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        if carry:
            result.append("1")

        result = int(''.join(result[::-1]), 2) & mask

        # 음수 처리
        if result > int_max:
            result = ~(result ^ mask)

        return result

    def getSum2(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a > int_max:
            a = ~(a ^ mask)
        
        return a


s = Solution()

a = 1
b = 2
#print(a, b, s.getSum1(a, b))
print(a, b, s.getSum2(a, b))

a = 2
b = 3
#print(a, b, s.getSum1(a, b))
print(a, b, s.getSum2(a, b))

a = 2
b = -1
#print(a, b, s.getSum1(a, b))
print(a, b, s.getSum2(a, b))