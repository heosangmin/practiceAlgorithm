'''
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createListNode(lst: List, index: int = 0) -> ListNode:
    if not lst:
        return None
    if index + 1 >= len(lst):
        return ListNode(lst[index])
    else:
        return ListNode(lst[index], createListNode(lst, index + 1))

def convertToList(ln: ListNode):
        lst = []
        node = ln
        while node:
            lst.append(node.val)
            node = node.next
        return lst

def printListNode(node: ListNode):
    print(node.val)
    if node.next:
        printListNode(node.next)
        
class Solution:
    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        
        return root.next

solution = Solution()
head, left, right = [1,2,3,4,5], 2, 4
ln = createListNode(head)
print(convertToList(solution.reverseBetween1(ln, left, right)))

head, left, right = [5], 1, 1
ln = createListNode(head)
print(convertToList(solution.reverseBetween1(ln, left, right)))