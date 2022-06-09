'''
2022/06/09

https://app.codesignal.com/interview-practice/task/oZXs4td52fsdWC9kR

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new t's root.
For example, removing 4 from the following tree has no effect because there is no such value in the tree:

    5
   / \
  2   6
 / \   \
1   3   8
       /
      7
Removing 5 causes 3 (the rightmost node in left subtree) to move to the root:

    3
   / \
  2   6
 /     \
1       8
       /
      7
And removing 6 after that creates the following tree:

    3
   / \
  2   8
 /   /
1   7
You're given a binary search tree t and an array of numbers queries. Your task is to remove queries[0], queries[1], etc., from t, step by step, following the algorithm above. Return the resulting BST.

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": 8,
            "left": {
                "value": 7,
                "left": null,
                "right": null
            },
            "right": null
        }
    }
}
and queries = [4, 5, 6], the output should be

solution(t, queries) = {
    "value": 3,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": null
    },
    "right": {
        "value": 8,
        "left": {
            "value": 7,
            "left": null,
            "right": null
        },
        "right": null
    }
}
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ t size ≤ 1000,
-109 ≤ node value ≤ 109.

[input] array.integer queries

An array that contains the numbers to be deleted from t.

Guaranteed constraints:
1 ≤ queries.length ≤ 1000,
-109 ≤ queries[i] ≤ 109.

[output] tree.integer

The tree after removing all the numbers in queries, following the algorithm above.
'''
from os import remove


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def map_to_Tree(m):
    tree = None
    if m:
        tree = Tree(m["value"])
        tree.left = map_to_Tree(m["left"])
        tree.right = map_to_Tree(m["right"])
    return tree

def Tree_to_list_preorder(tree:Tree, result_list):
    if tree:
        result_list.append(tree.value)
        Tree_to_list_preorder(tree.left, result_list)
        Tree_to_list_preorder(tree.right, result_list)
    return result_list

def solution(t, queries):
    def get_rightmost_value(t):
        if not t:
            return None
        while t.right:
            t = t.right
        return t.value
    
    def remove_rightmost(t):
        if not t.right:
            return t.left
        else:
            t.right = remove_rightmost(t.right)
        return t

    def bst(t, q):
        if not t:
            return None
        
        if t.value == q:
            if t.left:
                t.value = get_rightmost_value(t.left)
                t.left = remove_rightmost(t.left)
            else:
                t = t.right
        elif q < t.value :
            t.left = bst(t.left, q)
        else:
            t.right = bst(t.right, q)
        
        return t

    for q in queries:
        t = bst(t, q)
    
    return t

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": 8,
            "left": {
                "value": 7,
                "left": None,
                "right": None
            },
            "right": None
        }
    }
}
queries = [4, 5, 6]
print(Tree_to_list_preorder(solution(map_to_Tree(t), queries), []))