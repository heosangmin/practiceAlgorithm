'''
147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:
1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:
The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''

from ListNodeUtil import *
from typing import Optional

class Solution:
    def insertionSortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        책의 풀이
        삽입 정렬이 뭔지 몰라서 한참 찾아본 다음에서야 풀이를 시작했다.
        하지만 책 내용을 아무리 읽어봐도 무슨 말인지 알 수가 없다.
        처음부터 삽입 정렬과 관련 지어서 설명을 하든가.
        적힌 내용이라고는 자기가 쓴 코드를 풀어서 설명하는 것밖에 되지 않는다.
        코드 복기하는 것도 아니고.
        '''
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next

            cur = parent

        return parent.next

    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        다른 유저의 풀이
        https://leetcode.com/problems/insertion-sort-list/discuss/1176552/Python3-188ms-Solution-(explanation-with-visualization)
        '''
        if not head or not head.next:
            return head
        
        # head 앞에 가장 작은 값의 dummy_head를 두는 것이 도움됨.
        dummy_head = ListNode(val=-5000, next=head)
        last_sorted = head # 정렬된 부분의 마지막 노드
        cur = head.next # cur는 항상 last_sorted의 다음 노드가 되어야 함.(cur는 비교 대상 노드)

        while cur:
            if cur.val >= last_sorted.val:
                # 비교 대상인 cur의 값이 정렬된 값들의 마지막 노드 last_sorted의 값보다 크면
                # 정렬된 상태이므로 다음 노드(cur)로 last_sorted를 전진시킴.
                last_sorted = last_sorted.next
            else:
                # 비교 대상인 cur의 값이 정렬된 값들의 마지막 노드 last_sorted의 값보다 작으면
                # cur의 값을 삽입(insertion)할 위치를 제일 앞의 노드부터 탐색함.
                # 그 포인터인 prev는 가장 앞의 노드(dummy_head)부터 cur의 값보다 클때까지 전진한다.
                prev = dummy_head
                while prev.next.val <= cur.val: # prev 다음 노드의 값이 cur의 값보다 작으면
                    prev = prev.next # 삽입할 위치가 아니므로 prev를 전진시킨다.
                
                # 루프를 빠져나왔다는 것은 cur 값을 삽입할 위치가 되었다는 것이므로
                # prev와 prev.next 사이에 cur를 삽입한다.
                last_sorted.next = cur.next # 새 cur(last_sorted.next)는 현재 cur의 다음 노드가 됨.
                cur.next = prev.next 
                prev.next = cur
            
            # cur는 last_sorted의 다음 노드로서 새 비교대상이 됨.
            # 위에도 적었지만 cur는 항상 last_sorted의 다음 노드가 되어야 함.
            cur = last_sorted.next
        
        return dummy_head.next


head1 = [4,2,1,3]
head2 = [-1,5,3,4,0]

ln1 = createListNode(head1)
ln2 = createListNode(head2)

s = Solution()

# print(convertToList(s.insertionSortList1(ln1)))
# print(convertToList(s.insertionSortList1(ln2)))

print(convertToList(s.insertionSortList2(ln1)))
print(convertToList(s.insertionSortList2(ln2)))