'''
1038. Binary Search Tree to Greater Sum Tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Input: root = [0,null,1]
Output: [1,null,1]

Input: root = [1,0,2]
Output: [3,3,2]

Input: root = [3,2,4,1]
Output: [7,9,4,10]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 100
- All the values in the tree are unique.
- root is guaranteed to be a valid binary search tree.
'''

from TreeNodeUtil import TreeNode, convertTreeNodes, convertBfsList

class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        결과 트리를 새로 만들려고 하다보니 풀이가 생각나지 않았다.
        책의 풀이를 보니 결과 트리를 따로 만들지 않고 주어진 트리에 그대로 결과 값을 덮어쓰는 것으로 충분했다.
        '''
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root


root1 = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root2 = [0,None,1]
root3 = [1,0,2]
root4 = [3,2,4,1]

tn1 = convertTreeNodes(root1)
tn2 = convertTreeNodes(root2)
tn3 = convertTreeNodes(root3)
tn4 = convertTreeNodes(root4)

s1 = Solution()
s2 = Solution()
s3 = Solution()
s4 = Solution()

print(convertBfsList(s1.bstToGst(tn1)))
print(convertBfsList(s2.bstToGst(tn2)))
print(convertBfsList(s3.bstToGst(tn3)))
print(convertBfsList(s4.bstToGst(tn4)))