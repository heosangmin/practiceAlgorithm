'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Input: root = [1,2]
Output: [1,2]

Constraints:
- The number of nodes in the tree is in the range [0, 104].
- -1000 <= Node.val <= 1000
'''

from TreeNodeUtil import TreeNode, convertTreeNodes, convertBfsList
import collections
from typing import List, Optional

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ["#"]

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        
        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None

        nodes = data.split()
        root = TreeNode(nodes[1])
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] != "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        
        return root

root1 = [1,2,3,None,None,4,5]
root2 = []
root3 = [1]
root4 = [1,2]

ser = Codec()
deser = Codec()

ser1 = ser.serialize(convertTreeNodes(root1))
ser2 = ser.serialize(convertTreeNodes(root2))
ser3 = ser.serialize(convertTreeNodes(root3))
ser4 = ser.serialize(convertTreeNodes(root4))

print(convertBfsList(deser.deserialize(ser1)))
print(convertBfsList(deser.deserialize(ser2)))
print(convertBfsList(deser.deserialize(ser3)))
print(convertBfsList(deser.deserialize(ser4)))