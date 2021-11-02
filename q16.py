'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(l1: ListNode, l2: ListNode, co: int = 0):
            if l1 and not l2:
                val1, val2 = l1.val, 0
                next1, next2 = l1.next, None
            elif not l1 and l2:
                val1, val2 = 0, l2.val
                next1, next2 = None, l2.next
            else:
                val1, val2 = l1.val, l2.val
                next1, next2 = l1.next, l2.next
            
            sum = ListNode((val1 + val2 + co) % 10)
            co = (val1 + val2 + co) // 10

            if next1 and next2:
                sum.next = add(next1, next2, co)
            elif next1 and not next2:
                sum.next = add(next1, None, co)
            elif not next1 and next2:
                sum.next = add(None, next2, co)
            else:
                if co > 0:
                    sum.next = ListNode(co)
            return sum

        return add(l1, l2)

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        return self.toReverseLinkedList(str(resultStr))

    def addTwoNumbers3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next

    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head,None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReverseLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

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

solution = Solution()

l1 = [2,4,3]
l2 = [5,6,4]
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers1(ln1,ln2)))
print(convertToList(solution.addTwoNumbers2(ln1,ln2)))
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers3(ln1,ln2)))

l1 = [0]
l2 = [0]
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers1(ln1,ln2)))
print(convertToList(solution.addTwoNumbers2(ln1,ln2)))
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers3(ln1,ln2)))

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers1(ln1,ln2)))
print(convertToList(solution.addTwoNumbers2(ln1,ln2)))
ln1 = createListNode(l1)
ln2 = createListNode(l2)
print(convertToList(solution.addTwoNumbers3(ln1,ln2)))