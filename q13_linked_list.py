'''
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
'''

import collections
from typing import Deque, List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        node = head
        lst = []
        while node is not None:
            lst.append(node.val)
            node = node.next

        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False
        
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        dq = collections.deque()

        if not head:
            return True

        node = head
        while node:
            dq.append(node.val)
            node = node.next
        
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        
        return True


head = [1,2,2,1]
def createListNode(index: int) -> ListNode:
    if index + 1 >= len(head):
        return ListNode(head[index])
    else:
        return ListNode(head[index], createListNode(index + 1))

first = createListNode(0)

# def printListNode(node: ListNode):
#     print(node.val)
#     if node.next:
#         printListNode(node.next)

# printListNode(first)

solution = Solution()
print(solution.isPalindrome1(first))
print(solution.isPalindrome2(first))