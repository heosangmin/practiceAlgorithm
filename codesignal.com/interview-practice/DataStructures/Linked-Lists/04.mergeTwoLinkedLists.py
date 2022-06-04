'''
2022/06/04

https://app.codesignal.com/interview-practice/task/6rE3maCQwrZS3Mm2H

Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
solution(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
solution(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
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

# 오름차순으로 정렬된 두 연결 리스트를 병합하는 문제
# 시간 복잡도를 O(l1의 길이 + l2의 길이)로 제한하고 있다.
# 즉 각 리스트를 한 번씩만 순회해서 새 리스트를 만들어야 한다는 것.
# 문제의 난이도는 medium인데. 어떤 부분을 놓치고 있는 것 같다.
# 정렬되어 있는 상태의 두 리스트라면 노드 하나씩 비교해 가면서 새 리스트를 만들면 되지 않나?
def solution(l1, l2):
    head = result = ListNode(None)

    while l1 or l2:
        #print(l1.value if l1 else None, l2.value if l2 else None)

        if l1 and l2:
            
            if l1.value < l2.value:
                head.next = ListNode(l1.value)
                l1 = l1.next
            else:
                head.next = ListNode(l2.value)
                l2 = l2.next

        elif l1 and not l2:
            head.next = ListNode(l1.value)
            l1 = l1.next
        else:
            head.next = ListNode(l2.value)
            l2 = l2.next

        head = head.next

    return result.next


l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(ListNode_to_list(solution(list_to_ListNode(l1), list_to_ListNode(l2))))

l1 = [1, 1, 2, 4]
l2 = [0, 3, 5]
print(ListNode_to_list(solution(list_to_ListNode(l1), list_to_ListNode(l2))))
