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
        
def createTreeNodes(nodes: List):
    if not nodes:
        return []

    root = TreeNode(nodes[0])
    for i in range(1, len(nodes)):
        pass


root1 = [3,9,20,None,None,15,7]
root2 = [1,None,2]
root3 = []
root4 = [0]

s = Solution()
tn1 = TreeNode(root1[0])
#print(s.maxDepth(tn1))

print(createTreeNodes(root1))