'''
783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 100].
- 0 <= Node.val <= 105
'''

from typing import Optional
from TreeNodeUtil import *
import sys

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST1(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST1(root.left)
        
        #print(f"self.result={self.result}, root.val={root.val}, self.prev={self.prev}")
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST1(root.right)
        
        return self.result

    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node: TreeNode = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result

root1 = [4,2,6,1,3]
root2 = [1,0,48,None,None,12,49]
root3 = [8,4,12,2,6,None,None,1,3,5,7]

s1 = Solution()
s2 = Solution()
s3 = Solution()

# print(s1.minDiffInBST1(convertTreeNodes(root1)))
# print(s2.minDiffInBST1(convertTreeNodes(root2)))
# print(s3.minDiffInBST1(convertTreeNodes(root3)))

print(s1.minDiffInBST2(convertTreeNodes(root1)))
print(s2.minDiffInBST2(convertTreeNodes(root2)))
print(s3.minDiffInBST2(convertTreeNodes(root3)))