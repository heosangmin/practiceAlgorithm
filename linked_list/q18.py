'''
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106
'''


from typing import List, Optional


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
    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        odd = head
        even = head.next
        even_head = odd.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head

solution = Solution()
l1, l2 = [1,2,3,4,5], [2,1,3,5,6,4,7]
ln1, ln2 = createListNode(l1), createListNode(l2)

print(convertToList(solution.oddEvenList1(ln1)))
print(convertToList(solution.oddEvenList1(ln2)))