'''
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high]

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 104].
- 1 <= Node.val <= 105
- 1 <= low <= high <= 105
- All Node.val are unique.
'''

from TreeNodeUtil import TreeNode, convertBfsList, convertTreeNodes
from typing import Optional

class Solution:
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        재귀 dfs로 노드가 해당 범위의 값일 경우에만 반환 값을 더해서 리턴함.
        '''
        if not root:
            return 0

        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)

        if root.val >= low and root.val <= high:
            return root.val + l + r
        else:
            return l + r

    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        책의 재귀 dfs 풀이
        root.val if low <= root.val <= high else 0
        와 같은 표현이 가능하다는 게 재미있다.
        '''
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST2(root.left, low, high) + \
            self.rangeSumBST2(root.right, low, high)

    def rangeSumBST3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        책의 재귀 dfs 가지치기 풀이
        dfs로 탐색하되 low, high의 조건에 해당하지 않는 가지를 쳐내는 형태로 탐색에서 배제한다.
        '''
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def rangeSumBST4(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        책의 반복 dfs 가지치기 풀이
        위의 재귀 dfs와 조금 반대되는 상황이라 이해가 어렵다.
        위에서는 범위에 해당하지 않는 노드는 제외(val이 low보다 작을 경우 node.right으로 진입)했다면
        이번 풀이에서는 범위에 해당하는 노드를 stack에 쌓는다.(val이 low보다 클 경우 node.left를 stack에 append)
        '''
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

    def rangeSumBST5(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        책의 bfs 풀이
        bfs로도 상관 없다는 것이 의아했다.
        결국 탐색 순서와는 상관 없이 각 노드의 유효한 값만 더하면 되기 때문이다.
        '''
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

root1 = [10,5,15,3,7,None,18]
low1 = 7
high1 = 15

root2 = [10,5,15,3,7,13,18,1,None,6]
low2 = 6
high2 = 10

s1 = Solution()
s2 = Solution()

# print(s1.rangeSumBST1(convertTreeNodes(root1), low1, high1))
# print(s2.rangeSumBST1(convertTreeNodes(root2), low2, high2))

# print(s1.rangeSumBST2(convertTreeNodes(root1), low1, high1))
# print(s2.rangeSumBST2(convertTreeNodes(root2), low2, high2))

# print(s1.rangeSumBST3(convertTreeNodes(root1), low1, high1))
# print(s2.rangeSumBST3(convertTreeNodes(root2), low2, high2))

# print(s1.rangeSumBST4(convertTreeNodes(root1), low1, high1))
# print(s2.rangeSumBST4(convertTreeNodes(root2), low2, high2))

print(s1.rangeSumBST5(convertTreeNodes(root1), low1, high1))
print(s2.rangeSumBST5(convertTreeNodes(root2), low2, high2))