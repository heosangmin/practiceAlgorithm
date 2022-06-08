'''
2022/06/08

https://app.codesignal.com/interview-practice/task/mDpAJnDQkJqaYYsCg

Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

Example

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": None,
            "right": {
                "value": -1,
                "left": None,
                "right": None
            }
        }
    },
    "right": {
        "value": 7,
        "left": None,
        "right": None
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": -1,
            "left": None,
            "right": None
        }
    }
}
the output should be solution(t1, t2) = true.

This is what these trees look like:

      t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1
As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": {
                "value": -1,
                "left": None,
                "right": None
            },
            "right": None
        }
    },
    "right": {
        "value": 7,
        "left": None,
        "right": None
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": -1,
            "left": None,
            "right": None
        }
    }
}
the output should be solution(t1, t2) = false.

This is what these trees look like:

        t1:            t2:
         5             10
       /   \          /  \
     10     7        4    6
   /    \           / \    \
  4     6          1   2   -1
 / \   / 
1   2 -1
As you can see, there is no vertex v such that the subtree of t1 for vertex v equals t2.

For

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 2,
        "left": None,
        "right": None
    }
}
and

t2 = {
    "value": 2,
    "left": {
        "value": 1,
        "left": None,
        "right": None
    },
    "right": None
}
the output should be solution(t1, t2) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t1

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 6 · 104,
-1000 ≤ node value ≤ 1000.

[input] tree.integer t2

Another binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 6 · 104,
-1000 ≤ node value ≤ 1000.

[output] boolean

Return true if t2 is a subtree of t1, otherwise return false.
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
        tree.left = map_to_Tree(m["left"])
        tree.right = map_to_Tree(m["right"])
    # else:
    #     tree = Tree(None)
    return tree

def solution(t1, t2):

    if t1 is None and t2 is None:
        return True
    if t1 is None:
        return False
    if t2 is None:
        return True

    # def find_start(t1, t2):
    #     if t1.value == t2.value:
    #         return t1
    #     if t1.left:
    #         node = find_start(t1.left, t2)
    #         if node:
    #             return node
    #     if t1.right:
    #         node = find_start(t1.right, t2)
    #         if node:
    #             return node
    
    # start = find_start(t1, t2)
    
    def compare(t1, t2):
        if t1 and t2:
            return t1.value == t2.value and \
                compare(t1.left, t2.left) and \
                compare(t1.right, t2.right)
        elif not t1 and not t2:
            return True
        else:
            return False

    return compare(t1, t2) or solution(t1.left, t2) or solution(t1.right, t2)
    

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": None,
            "right": {
                "value": -1,
                "left": None,
                "right": None
            }
        }
    },
    "right": {
        "value": 7,
        "left": None,
        "right": None
    }
}
t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": -1,
            "left": None,
            "right": None
        }
    }
}
print(solution(map_to_Tree(t1), map_to_Tree(t2))) # True

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": {
                "value": -1,
                "left": None,
                "right": None
            },
            "right": None
        }
    },
    "right": {
        "value": 7,
        "left": None,
        "right": None
    }
}
t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": -1,
            "left": None,
            "right": None
        }
    }
}
print(solution(map_to_Tree(t1), map_to_Tree(t2))) # False

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 2,
        "left": None,
        "right": None
    }
}
t2 = None
print(solution(map_to_Tree(t1), map_to_Tree(t2))) # True

t1 = None
t2 = {
    "value": 2,
    "left": None,
    "right": None
}
print(solution(map_to_Tree(t1), map_to_Tree(t2))) # False