'''
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Input: root = [5,4,5,1,1,5]
Output: 2

Input: root = [1,4,5,4,4,5]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 104].
- -1000 <= Node.val <= 1000
- The depth of the tree will not exceed 1000.
'''

from typing import Optional, List
import collections

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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath1(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node: TreeNode):
            if not node:
                return 0

            nonlocal count
            
            # 존재하지 않는 노드까지 DFS 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드와 자식 노드의 값이 동일한 경우 거리 +1
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽, 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            count = max(count, left + right)

            # 자식 노드 중 더 큰 값 리턴
            return max(left, right)

        dfs(root)

        return count


root1 = [5,4,5,1,1,5]
root2 = [1,4,5,4,4,5]
root3 = [1,None,1,1,1,1,1,1]

tn1 = convertTreeNodes(root1)
tn2 = convertTreeNodes(root2)
tn3 = convertTreeNodes(root3)

s = Solution()
# print(s.longestUnivaluePath1(tn1))
# print(s.longestUnivaluePath1(tn2))
print(s.longestUnivaluePath1(tn3))