'''
148. Sort List
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []


Constraints:
- The number of nodes in the list is in the range [0, 5 * 104].
- -105 <= Node.val <= 105
'''

from typing import Optional
from ListNodeUtil import *

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        l1과 l2 값을 비교, 정렬해서 병합 후 리턴한다.
        '''
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        '''
        l1 or l2
        1. l1이 있으면 l1을 리턴함(l2 유무 상관 없이)
        2. l1이 없으면 l2를 리턴함
        '''
        return l1 or l2

    # 병합 정렬
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        '''
        런너 기법 활용
        분할 정복(Divide and Conquer)을 위해서는 중앙을 분할(Divide)해야 한다.
        런너 fast가 끝에 도달할 때 slow는 중앙에 도착한다. half는 slow 이전 값으로 한다.
        마지막에 half.next = None으로 half 위치를 기준으로 연결 리스트 관계를 끊어버린다.
        '''
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        '''
        분할 재귀 호출
        중앙인 slow를 기준으로 두 연결 리스트(head, slow)를 재귀 호출로 분할해 나가면 결국 단일 아이템으로 쪼개진다.
        '''
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        '''
        정렬 및 리스트 병합 리턴
        '''
        return self.mergeTwoLists(l1, l2)

class Solution2:
    # 내장 함수(팀소트) 사용
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        
        return head

head1 = [4,2,1,3]
head2 = [-1,5,3,4,0]
head3 = []

ln1 = createListNode(head1)
ln2 = createListNode(head2)
ln3 = createListNode(head3)

s1 = Solution1()
s2 = Solution2()

# print(convertToList(s1.sortList(ln1)))
# print(convertToList(s1.sortList(ln2)))
# print(convertToList(s1.sortList(ln3)))

print(convertToList(s2.sortList(ln1)))
print(convertToList(s2.sortList(ln2)))
print(convertToList(s2.sortList(ln3)))