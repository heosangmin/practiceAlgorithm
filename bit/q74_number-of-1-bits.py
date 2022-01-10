'''
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32.
'''

class Solution:
    # 문제 설명에도 나와 있지만 자바에서는 unsigned int 타입이 없기 때문에 까다로울 것 같다.
    def hammingWeight1(self, n: int) -> int:
        # 0으로 구성된 비트들과의 해밍 거리로 볼 수 있다.
        # 따라서 32 비트의 0들과의 XOR 연산 결과에서 1을 카운트하면 된다.
        
        # bin(n ^ 0b00000000000000000000000000000000).count("1")
        # 또는
        # bin(n ^ 0).count("1")
        # 도 옳다.

        return bin(n).count("1")

    def hammingWeight2(self, n: int) -> int:
        '''
        bin() 덕분에 문자열로 처리하면 너무 쉽게 해결되기 때문에 원래의 취지를 생각해보자.
        이진수의 특징인데,
        1000에서 1을 빼면 0111이 된다. 이 두 값을 AND 연산하면 0000이 된다.
        1010에서 1을 빼면 1001이 된다. 이 두 값을 AND 연산하면 1000이 된다.
        1011에서 1을 빼면 1010이 된다. 이 두 값을 AND 연산하면 1010이 된다.
        즉 원래 값에서 1을 뺀 값과 AND 연산을 하게 되면 1 비트씩 감소한다.
        이 계산을 값이 0이 될 때까지 반복하면 그 반복 수가 1 비트의 개수가 된다.
        '''
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

s = Solution()

n = 0b00000000000000000000000000001011
#print(n, s.hammingWeight1(n))
print(n, s.hammingWeight2(n))

n = 0b00000000000000000000000010000000
#print(n, s.hammingWeight1(n))
print(n, s.hammingWeight2(n))

n = 0b11111111111111111111111111111101
#print(n, s.hammingWeight1(n))
print(n, s.hammingWeight2(n))