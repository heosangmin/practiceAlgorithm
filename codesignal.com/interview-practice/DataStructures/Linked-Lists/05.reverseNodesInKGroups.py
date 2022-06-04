'''
2022/06/04

https://app.codesignal.com/interview-practice/task/XP2Wn9pwZW6hvqH67

Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
solution(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
solution(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
solution(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
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

def solution(l, k):
    
    if not l:
        return l
    
    c = l
    n = k
    while c and n:
        c = c.next
        n -= 1
    if n:
        return l

    curr = l
    next = None
    prev = None
    n = k
    while curr and n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n -= 1
    
    if next:
        l.next = solution(next, k)
    
    return prev

print(ListNode_to_list(solution(list_to_ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),3)))