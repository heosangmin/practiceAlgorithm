'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists1(l1.next, l2)
        return l1

    def mergeTwoLists2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1: List = self.convertToList(l1)
        lst2: List = self.convertToList(l2)    
        concated = lst1 + lst2
        concated.sort()
        return self.createListNode(concated, 0)

    def convertToList(self, ln: ListNode):
        lst = []
        node = ln
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def createListNode(self, lst: List, index: int) -> ListNode:
        if not lst:
            return None
        if index + 1 >= len(lst):
            return ListNode(lst[index])
        else:
            return ListNode(lst[index], self.createListNode(lst, index + 1))

    def printListNode(self, node: ListNode):
        print(node.val)
        if node.next:
            self.printListNode(node.next)


solution = Solution()

l1 = [1,2,4]
l2 = [1,3,4]
 
ln1 = solution.createListNode(l1, 0)
ln2 = solution.createListNode(l2, 0)

solution.printListNode(solution.mergeTwoLists1(ln1, ln2))
#solution.printListNode(solution.mergeTwoLists2(ln1, ln2))
