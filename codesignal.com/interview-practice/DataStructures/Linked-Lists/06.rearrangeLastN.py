'''
2022/06/04

https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt

Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
solution(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
solution(l, n) = [7, 1, 2, 3, 4, 5, 6].
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

# def solution(l, n):
#     if not l or n == 0:
#         return l

#     first = l

#     def helper(l, n):
#         if l.next == None:
#             return None, l, n-1
        
#         new_first, last, m = helper(l.next, n)

#         if m == 0:
#             new_first = l.next
#             l.next = None

#         return new_first, last, m-1
        
#     new_first, last, m = helper(l, n)

#     if m == 0:
#         return l

#     last.next = first

#     return new_first

def solution(l, n):
    if n == 0:
        return l
    
    front, back = l, l
    for _ in range(n):
        front = front.next

    if not front:
        return l

    while front.next:
        front = front.next
        back = back.next

    new_start = back.next
    back.next = None
    front.next = l

    return new_start


print(ListNode_to_list(solution(list_to_ListNode([1, 2, 3, 4, 5]), 3))) # [3, 4, 5, 1, 2]
print(ListNode_to_list(solution(list_to_ListNode([1, 2, 3, 4, 5, 6, 7]), 1))) # [7, 1, 2, 3, 4, 5, 6]
print(ListNode_to_list(solution(list_to_ListNode([123, 456, 789, 0]), 4))) # [123, 456, 789, 0]