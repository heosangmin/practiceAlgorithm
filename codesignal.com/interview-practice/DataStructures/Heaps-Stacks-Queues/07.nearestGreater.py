'''
2022/06/13

https://app.codesignal.com/interview-practice/task/ndve2n4KH7dPBksLh

Given an array of integers a, return a new array b using the following guidelines:

For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
If there are two options for bi, put the leftmost one in bi.
If there are no options for bi, put -1 in bi.
Example

For a = [1, 4, 2, 1, 7, 6], the output should be
solution(a) = [1, 4, 1, 2, -1, 4].

for a[0], the nearest larger element is 4 at index a[1] -> b[0] contains the value 1.
for a[1], the nearest larger element is 7 at a[4] -> b[1] contains the value 4.
for a[2], the nearest larger element is 4 at a[1] (7 is also larger, but 4 has the minimal position) -> b[2] contains the value 1.
for a[3], the nearest larger element is 2 at a[2] (7 is also larger, but 2 has the minimal position) -> b[3] contains the value 2.
for a[4], there is no element larger than 7 -> b[4] contains the value -1.
for a[5], the nearest larger element is 7 at a[4] -> b[5] contains the value 4.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An unsorted array of integers.

Guaranteed constraints:
1 ≤ a.length ≤ 4 · 104,
1 ≤ a[i] ≤ 109.

[output] array.integer

An array b, where for each index i, bi is the index of the nearest number in a that is greater than ai.
'''

# gustavomirandag's solution
def solution(a):
  b, stack = [-1] * len(a), []
  for i in range(len(a)):
    while stack and a[stack[-1]] < a[i]:
      j = stack.pop()
      if b[j] == -1 or i - j < j - b[j]: b[j] = i
    if not stack: b[i] = -1
    else: b[i] = stack[-1] if a[i] != a[stack[-1]] else b[stack[-1]]    
    stack.append(i)
  return b

a = [1, 4, 2, 1, 7, 6]
print(solution(a)) # [1, 4, 1, 2, -1, 4]