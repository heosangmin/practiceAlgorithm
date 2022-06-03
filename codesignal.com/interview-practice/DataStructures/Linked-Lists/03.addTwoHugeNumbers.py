'''
2022/06/03

https://app.codesignal.com/interview-practice/task/RvDFbsNC3Xn7pnQfH/description

You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
solution(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
solution(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.
'''
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def list_to_ListNode(l):
    if not l:
        return None
    head = ListNode(l[0])
    tail = head
    for i in range(1, len(l)):
        tail.next = ListNode(l[i])
        tail = tail.next
    return head

def ListNode_to_list(ln):
    l = []
    while ln:
        l.append(ln.value)
        ln = ln.next
    return l

# def solution(a, b):
#     lst1, lst2 = [], []
#     while a:
#         lst1.append(a.value)
#         a = a.next
#     while b:
#         lst2.append(b.value)
#         b = b.next
    
#     for i in range(len(lst1)):
#         lst1[i] = str(lst1[i]).zfill(4)
#     for i in range(len(lst2)):
#         lst2[i] = str(lst2[i]).zfill(4)

#     sum_of_nums = str(int("".join(lst1)) + int("".join(lst2)))
#     if len(sum_of_nums) % 4 != 0:
#         sum_of_nums = "0" * (4 - int(len(sum_of_nums) % 4)) + sum_of_nums
    
#     head = tail = ListNode(None)
#     for i in range(0, len(sum_of_nums), 4):
#         tail.next = ListNode(int(sum_of_nums[i:i+4]))
#         tail = tail.next
    
#     return head.next

'''
무식하게 리스트로 변환해서 처리하면 위와 같이 할 수 있지만
사실 문제에서 원하는 것은 연결 리스트 그대로의 연산일 듯.

다른 사람 풀이에서 괜찮은 걸 발견했다.

1. 입력 받은 연결 리스트를 뒤집는다.
2. a, b의 각 노드를 순서대로 더한다.
3. 10000 이상일 경우 올림수로 1을 넘기고 나머지를 결과 노드로 저장한다.
'''
def solution(a, b):
    a = reverse_ListNode(a)
    b = reverse_ListNode(b)

    carry = 0
    result: ListNode = None
    while a or b or carry > 0:
        temp = ((a.value if a is not None else 0) + 
                (b.value if b is not None else 0) +
                carry)
        
        carry = temp // 10000
        node = ListNode(temp % 10000)
        node.next = result
        result = node

        if a:
            a = a.next
        if b:
            b = b.next

    return result


def reverse_ListNode(node):
    curr = node
    prev = None
    while curr:
        prev, curr.next, curr = curr, prev, curr.next
    return prev

print(ListNode_to_list(solution(list_to_ListNode([9876, 5432, 1999]), list_to_ListNode([1, 8001])))) # [9876, 5434, 0]
print(ListNode_to_list(solution(list_to_ListNode([123, 4, 5]), list_to_ListNode([100, 100, 100])))) # [223, 104, 105]