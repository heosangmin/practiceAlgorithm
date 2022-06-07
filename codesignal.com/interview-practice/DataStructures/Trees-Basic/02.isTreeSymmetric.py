'''
2022/06/07

https://app.codesignal.com/interview-practice/task/tXN6wQsTknDT6bNrf

Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.
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

def check_symmetric(subtree0, subtree1):
    
    if subtree0 is None and subtree1 is None:
        return True
    elif subtree0 is not None and subtree1 is not None:
        return subtree0.value == subtree1.value and \
            check_symmetric(subtree0.left, subtree1.right) and \
            check_symmetric(subtree0.right, subtree1.left)
    return False # 한쪽만 있는 경우

def solution(t):
    return t is None or check_symmetric(t.left, t.right)



t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

print(solution(map_to_Tree(t))) # True

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

print(solution(map_to_Tree(t))) # False