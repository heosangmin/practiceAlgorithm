'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Input: root = []
Output: 0

Input: root = [0]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100
'''

from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 0
        Q = collections.deque([root])
        while Q:
            depth += 1
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return depth
        
def convertTreeNodes(nodes: List):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    Q = collections.deque([root])
    nodes_len = len(nodes)

    for i in range(1, nodes_len+1, 2):
        node = Q.popleft()
        if i < nodes_len and nodes[i] is not None:
            left = TreeNode(nodes[i])
            node.left = left
            Q.append(left)

        if i+1 < nodes_len and nodes[i+1] is not None:
            right = TreeNode(nodes[i+1])
            node.right = right
            Q.append(right)

    return root

def convertList(root: TreeNode):
    Q = collections.deque([root])
    nodes = []
    while Q:
        node = Q.popleft()
        nodes.append(node.val)
        print("root:",node.val)
        
        if node.left:
            Q.append(node.left)
            print("left:",node.left.val)
            #nodes.append(node.left.val)
        else:
            nodes.append(None)

        if node.right:
            Q.append(node.right)
            print("right:",node.right.val)
            #nodes.append(node.right.val)
        else:
            nodes.append(None)
    
    return nodes

root1 = [3,9,20,None,None,15,7]
root2 = [1,None,2]
root3 = []
root4 = [0]

s = Solution()
tn1 = TreeNode(root1[0])

tree_node_1 = convertTreeNodes(root1)
tree_node_2 = convertTreeNodes(root2)
tree_node_3 = convertTreeNodes(root3)
tree_node_4 = convertTreeNodes(root4)
#print(convertList(tree_node_1))
print(s.maxDepth(tree_node_1))
print(s.maxDepth(tree_node_2))
print(s.maxDepth(tree_node_3))
print(s.maxDepth(tree_node_4))
