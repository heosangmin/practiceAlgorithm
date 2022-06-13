'''
2022/06/13

https://app.codesignal.com/interview-practice/task/gnZYGn367s4yaHvRr

Note: Write a solution with O(operations.length) complexity, since this is what you would be asked to do during a real interview.

Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.

Example

For operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"], the output should be
solution(operations) = [10, 5, 5, 5, 10].

The operations array contains 5 instances of the min operation. The results array contains 5 numbers, each representing the minimum element in the stack at the moment when min was called.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string operations

An array of operations consistently applied to the stack. For each valid i, operations[i] is one of the following operations:

push x: add the number x to the stack;
pop: remove an element from the top of the stack;
min: find the minimum element from the current stack elements.
It is guaranteed that pop and min are not applied to an empty stack. It is also guaranteed that all of the numbers in the stack are positive and not greater than 109.
Guaranteed constraints:
1 ≤ operations.length ≤ 104.

[output] array.integer

For each min operation, return the minimum element from the current stack elements at the moment when the operation was called.
'''

# 명령 길이만큼의 복잡도를 걍제하고 있는데 다시 말해 min을 구하기 위해 스택을 탐색하면 안 된다는 소리다.
# 스택 두 개를 사용하면 쉽게 해결되지만 요구사항에 맞는 것일까.
def solution(operations):
    stack = []
    min_stack = []
    result = []
    for o in operations:
        # print(stack, min_stack)
        if o == "min":
            if len(min_stack) == 0:
                result.append(None)
            else:
                result.append(min_stack[-1])
        elif o == "pop":
            stack.pop()
            min_stack.pop()
        else:
            num = int(o.split()[1])
            stack.append(num)
            if len(min_stack) == 0:
                min_stack.append(num)
            else:
                min_stack.append(min(num, min_stack[-1]))
    return result

operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]

print(solution(operations))# [10, 5, 5, 5, 10]