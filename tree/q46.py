'''
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:
- The number of nodes in both trees is in the range [0, 2000].
- -104 <= Node.val <= 104
'''

from typing import Optional

from TreeNodeUtil import TreeNode,convertTreeNodes,convertBfsList

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        지금껏 반복보다 재귀가 더 익숙했다고 하지만 문제를 풀수록 전혀 그렇지 않음을 알았다.
        이렇게 간단하게 풀리는 문제를 가지고 한 시간은 엉뚱한 방향으로 고민했다.
        '''
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            '''
            A or B 가 둘 중 False가 아닌 값만 리턴하는 줄은 몰랐다.
            '''
            return root1 or root2

s = Solution()

root11 = [1,3,2,5]
root12 = [2,1,3,None,4,None,7]
root21 = [1]
root22 = [1,2]

tn11 = convertTreeNodes(root11)
tn12 = convertTreeNodes(root12)
tn21 = convertTreeNodes(root21)
tn22 = convertTreeNodes(root22)

print(convertBfsList(s.mergeTrees(tn11, tn12)))
print(convertBfsList(s.mergeTrees(tn21, tn22)))