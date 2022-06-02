'''
2022/06/02

https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description

Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
solution(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
solution(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
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

def print_ListNode(ln):
    while ln:
        print(ln.value, end=' ')
        ln = ln.next

def solution(l, k):
    head = ListNode(None)
    start = head
    head.next = l
    while head.next:
        if head.next.value == k:
            head.next = head.next.next
        else:
            head = head.next
    return start.next
        

l = list_to_ListNode([3, 1, 2, 3, 4, 5])
print(ListNode_to_list(solution(l, 3))) # [1, 2, 4, 5]

l = list_to_ListNode([1, 2, 3, 4, 5, 6, 7])
print(ListNode_to_list(solution(l, 10))) # [1, 2, 3, 4, 5, 6, 7]

l = list_to_ListNode([1000, 1000])
print(ListNode_to_list(solution(l, 1000))) # []