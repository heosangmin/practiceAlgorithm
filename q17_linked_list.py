'''
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

from typing import List, Optional


# Definition for singly-linked list.
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
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def swap(node: ListNode) -> ListNode:
            if not node or not node.next:
                return node

            temp = node.next
            node.next = node.next.next
            node, temp.next = temp, node

            if node.next.next:
                node.next.next = swap(node.next.next)

            return node

        return swap(head)

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            pair = head.next
            head.next = self.swapPairs2(pair.next)
            pair.next = head
            return pair
        return head

    def swapPairs3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

    def swapPairs4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

solution = Solution()

l1 = [1,2,3,4]
l2 = []
l3 = [1]

ln1,ln2,ln3 = createListNode(l1),createListNode(l2),createListNode(l3)
print(convertToList(solution.swapPairs1(ln1)))
print(convertToList(solution.swapPairs1(ln2)))
print(convertToList(solution.swapPairs1(ln3)))

ln1,ln2,ln3 = createListNode(l1),createListNode(l2),createListNode(l3)
print(convertToList(solution.swapPairs2(ln1)))
print(convertToList(solution.swapPairs2(ln2)))
print(convertToList(solution.swapPairs2(ln3)))

ln1,ln2,ln3 = createListNode(l1),createListNode(l2),createListNode(l3)
print(convertToList(solution.swapPairs3(ln1)))
print(convertToList(solution.swapPairs3(ln2)))
print(convertToList(solution.swapPairs3(ln3)))

ln1,ln2,ln3 = createListNode(l1),createListNode(l2),createListNode(l3)
print(convertToList(solution.swapPairs4(ln1)))
print(convertToList(solution.swapPairs4(ln2)))
print(convertToList(solution.swapPairs4(ln3)))