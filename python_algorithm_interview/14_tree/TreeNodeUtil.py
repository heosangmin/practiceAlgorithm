from typing import List
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

def convertBfsList(root: TreeNode) -> List:
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