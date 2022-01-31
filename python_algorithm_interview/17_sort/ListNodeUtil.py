from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createListNode(lst: List, index: int = 0) -> ListNode:
    if not lst:
        return None

    # legacy    
    # if index + 1 >= len(lst):
    #     return ListNode(lst[index])
    # else:
    #     return ListNode(lst[index], createListNode(lst, index + 1))
    
    # 파이썬 리스트 -> 연결 리스트
    head = ListNode()
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        if i+1 < len(lst):
            p.next = ListNode()
            p = p.next

    return head

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