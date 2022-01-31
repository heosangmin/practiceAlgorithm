'''
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''
from typing import List

class Solution:
    '''
    - 연산자인지 확인하는 방법이 순간 떠오르지 않았다. 파이썬의 편리함이 이런 데서 나온다. value in "+-*"라니.
    - isdigit()같은 흔하게 쓰일 거 같은 함수들이 바로 떠오르지 않아서 답답하다.
    - eval() 함수도 유용하다.
    - result.append()가 아니고 result.extend()하는 것에 유의하자.
      복수 개의 연산 결과가 리턴될 수 있으므로 결과 리스트를 result에 추가가 아닌 확장으로 붙여야 한다.

    계산 과정을 하나씩 따라가보면 왜 이렇게 풀리는지 이해가 가지만
    아직도 내 방식대로 풀려고 하면 해법이 생각나지 않는다. 큰일이다.
    '''
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, op, right) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result
        
        if expression.isdigit(): # 최종 형태(숫자 하나)인 경우 int로 변환해 리턴함.
            return [int(expression)]
        
        result = []
        for index, value in enumerate(expression):
            if value in "+-*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
            
                result.extend(compute(left, value, right))

        return result

s = Solution()

expression = "2-1-1"
print(expression, s.diffWaysToCompute(expression))

expression = "2*3-4*5"
print(expression, s.diffWaysToCompute(expression))