'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None) -> Optional[ListNode]:
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

def createListNode(lst: List, index: int = 0) -> ListNode:
    if not lst:
        return None
    if index + 1 >= len(lst):
        return ListNode(lst[index])
    else:
        return ListNode(lst[index], createListNode(lst, index + 1))

def printListNode(node: ListNode):
    print(node.val)
    if node.next:
        printListNode(node.next)

solution = Solution()

head1 = [1,2,3,4,5]
ln1 = createListNode(head1)
printListNode(solution.reverseList1(ln1))
ln1 = createListNode(head1)
printListNode(solution.reverseList2(ln1))