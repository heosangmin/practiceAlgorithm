'''
706. Design HashMap
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map contains the mapping for the ke

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
- 0 <= key, value <= 106
- At most 104 calls will be made to put, get, and remove.
'''
from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            if node.next is None:
                break
            node = node.next
        node.next = ListNode(key,value)
            

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        node = self.table[index]
        
        # 인덱스의 첫 번째 노드일 때
        if node.key == key:
            self.table[index] = ListNode() if node.next is None else node.next
            return
        
        # 첫 번쨰가 아닐 때
        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev, node = node, node.next


myHashMap = MyHashMap()
print(myHashMap.put(1, 1)) # The map is now [[1,1]]
print(myHashMap.put(2, 2)) # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(myHashMap.put(2, 1)) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
print(myHashMap.remove(2)) # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]