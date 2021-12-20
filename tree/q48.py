'''
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -104 <= Node.val <= 104
'''

from TreeNodeUtil import TreeNode,convertTreeNodes
from typing import Optional
import collections

class Solution:
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        '''
        dfs 탐색으로 각 노드의 높이를 반환하도록 한다.
        노드의 반환된 좌우 자식 노드의 높이 차이를 diff에 따로 저장하고 1을 초과하면 False를 리턴하도록 하는데
        좌우 자식 노드의 높이 차이가 2 이상이 된다면 그 시점에서 멈추도록 하면 더 좋을 것이다.
        그러려면 재귀가 아닌 반복으로 해야할까.
        '''
        if not root:
            return True
        
        diff = 0

        def dfs(node: TreeNode):
            nonlocal diff
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            #print(node.val, left, right, abs(left-right))
            diff = max(diff, abs(left-right))

            return max(left+1, right+1)

        dfs(root)
        return diff <= 1

    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        '''
        책에 나온 방법
        좌우의 자식 노드 높이를 비교하는데
        높이 차이가 1을 초과하게 되면 ( abs(left - right) > 1 )
        -1을 반환하고, 계속해서 -1을 반환하도록 한다.

        앞의 방법에서 내가 풀이한 것보다 비교 연산을 덜 하고, 공간적인 면에서도 낫다.
        '''
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        return check(root) != -1

root1 = [3,9,20,None,None,15,7]
root2 = [1,2,2,3,3,None,None,4,4]
root3 = []
root4 = [1,2,2,3,None,None,3,4,None,None,4]

tn1 = convertTreeNodes(root1)
tn2 = convertTreeNodes(root2)
tn3 = convertTreeNodes(root3)
tn4 = convertTreeNodes(root4)

s = Solution()

print(s.isBalanced1(tn1))
print(s.isBalanced1(tn2))
print(s.isBalanced1(tn3))
print(s.isBalanced1(tn4))

print(s.isBalanced2(tn1))
print(s.isBalanced2(tn2))
print(s.isBalanced2(tn3))
print(s.isBalanced2(tn4))