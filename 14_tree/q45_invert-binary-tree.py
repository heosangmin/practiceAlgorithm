'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
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

def printBfs(root: TreeNode):
    if not root:
        return []

    Q = collections.deque([root])
    result = []
    while Q:
        node = Q.popleft()
        result.append(node.val)
        
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
    
    return result

class Solution:
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        리프 노드까지 내려갔다가 좌우를 스왑하며 돌아오는 Bottom-Up 방식으로 풀었다.
        앞의 문제를 풀이해 오면서 내부 함수를 쓰는 것에 익숙해졌다.
        풀이는 됐지만 굳이 이렇게 할 필요는 없었다.
        '''
        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left
            return
        
        dfs(root)
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        책에 나온 Pythonic한 방법이다.
        보고 있자니 착찹해진다.
        '''
        if root:
            root.left, root.right = self.invertTree2(root.right), self.invertTree2(root.left)
            return root
        return None

    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        책에 나온 반복 구조 BFS를 이용한 풀이
        '''
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
            
        return root

    def invertTree4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        책에 나온 반복 구조 DFS를 이용한 풀이
        DFS로 바꾸기 위해 위의 BFS에서 큐 대신 스택으로 리스트 사용법만 변경함.
        '''
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
            
        return root

    def invertTree5(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        책에 나온 반복 구조 DFS 후위 순회를 이용한 풀이
        좌우 스왑을 언제 하는 지가 다른 버전인데,
        앞에서는 자식 노드 탐색을 들어가기 전에 스왑하고
        이번에는 리프까지 간 뒤에 스왑을 시작해 돌아오는 방식이다.
        '''
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            if node:

                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left
            
        return root

root1 = [4,2,7,1,3,6,9]
root2 = [2,1,3]
root3 = []

tn1 = convertTreeNodes(root1)
tn2 = convertTreeNodes(root2)
tn3 = convertTreeNodes(root3)

s = Solution()

# print(printBfs(s.invertTree1(tn1)))
# print(printBfs(s.invertTree1(tn2)))
# print(printBfs(s.invertTree1(tn3)))

# print(printBfs(s.invertTree2(tn1)))
# print(printBfs(s.invertTree2(tn2)))
# print(printBfs(s.invertTree2(tn3)))

# print(printBfs(s.invertTree3(tn1)))
# print(printBfs(s.invertTree3(tn2)))
# print(printBfs(s.invertTree3(tn3)))

# print(printBfs(s.invertTree4(tn1)))
# print(printBfs(s.invertTree4(tn2)))
# print(printBfs(s.invertTree4(tn3)))

print(printBfs(s.invertTree5(tn1)))
print(printBfs(s.invertTree5(tn2)))
print(printBfs(s.invertTree5(tn3)))