'''
2022/06/07

https://app.codesignal.com/interview-practice/task/TG4tEMPnAc3PnzRCs

Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}

s = 7

-> True
'''

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def map_to_Tree(m):
    tree = None
    if m:
        tree = Tree(m["value"])
        if m["left"]:
            tree.left = map_to_Tree(m["left"])
        if m["right"]:
            tree.right = map_to_Tree(m["right"])
    return tree

def traversal_preorder(tree:Tree, result_list):
    if tree:
        result_list.append(tree.value)
        traversal_preorder(tree.left, result_list)
        traversal_preorder(tree.right, result_list)
    return result_list

# def solution(t, s):
    
#     def traversal(node, s, sub_total):
#         if node:
#             if node.left is None and node.right is None: # this is leaf node
#                 return (node.value + sub_total) == s
#             else:
#                 result_left = traversal(node.left, s, node.value + sub_total)
#                 result_right = traversal(node.right, s, node.value + sub_total)
#                 return result_left or result_right
#         return False
            
#     return traversal(t, s, 0)

def solution(t, s):
    if t:
        if t.left is None and t.right is None:
            return s == t.value
        return solution(t.left, s - t.value) or solution(t.right, s - t.value)
    return False


t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        },
        "right": None
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": -3,
                "left": None,
                "right": None
            }
        }
    }
}
s = 7

# print(traversal_preorder(map_to_Tree(t), []))
# print(solution(map_to_Tree(t),s))

t = {
    "value": 5,
    "left": {
        "value": 7,
        "left": None,
        "right": None
    },
    "right": None
}
s = 5
print(solution(map_to_Tree(t),s)) # false