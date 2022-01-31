'''
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:
- MyCircularDeque(int k) Initializes the deque with a maximum size of k.
- boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
- boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
- boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
- boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
- int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
- int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
- boolean isEmpty() Returns true if the deque is empty, or false otherwise.
- boolean isFull() Returns true if the deque is full, or false otherwise.

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
- MyCircularDeque myCircularDeque = new MyCircularDeque(3);
- myCircularDeque.insertLast(1);  // return True
- myCircularDeque.insertLast(2);  // return True
- myCircularDeque.insertFront(3); // return True
- myCircularDeque.insertFront(4); // return False, the queue is full.
- myCircularDeque.getRear();      // return 2
- myCircularDeque.isFull();       // return True
- myCircularDeque.deleteLast();   // return True
- myCircularDeque.insertFront(4); // return True
- myCircularDeque.getFront();     // return 4
'''

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new:ListNode):
        tmp = node.right
        node.right = new
        new.left, new.right = node, tmp
        tmp.left = new
    
    def _del(self, node: ListNode):
        tmp = node.right.right
        node.right = tmp
        tmp.left = node

    def insertFront(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.k == self.len
        


# Your MyCircularDeque object will be instantiated and called as such:
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# [null, true, true, true, false, 2, true, true, true, 4]
obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getFront())
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
# param_3 = obj.deleteFront()
print(obj.getFront())
# param_7 = obj.isEmpty()