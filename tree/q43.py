'''
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 104].
- -100 <= Node.val <= 100
'''

from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    longest: int = 0

    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node: TreeNode) -> int:
            nonlocal diameter
            if not node:
                return 0
            
            height_left = dfs(node.left)
            height_right = dfs(node.right)

            diameter = max(diameter, height_left + height_right)
            return 1 + max(height_left, height_right)

        dfs(root)

        return diameter

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1
        
        dfs(root)
        return self.longest

    def diameterOfBinaryTree3(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node: TreeNode) -> int:
            
            nonlocal diameter

            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter = max(diameter, left_height + right_height)

            return max(left_height,right_height) + 1
        
        dfs(root)
        return diameter
        

root1 = [1,2,3,4,5]
root2 = [1,2]
root3 = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]

s = Solution()

print(s.diameterOfBinaryTree1(convertTreeNodes(root1)))
print(s.diameterOfBinaryTree1(convertTreeNodes(root2)))
print(s.diameterOfBinaryTree1(convertTreeNodes(root3)))

# print(s.diameterOfBinaryTree2(convertTreeNodes(root1)))
# print(s.diameterOfBinaryTree2(convertTreeNodes(root2)))
# print(s.diameterOfBinaryTree2(convertTreeNodes(root3)))

# print(s.diameterOfBinaryTree3(convertTreeNodes(root1)))
# print(s.diameterOfBinaryTree3(convertTreeNodes(root2)))
# print(s.diameterOfBinaryTree3(convertTreeNodes(root3)))