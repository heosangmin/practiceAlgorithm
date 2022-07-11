'''
The sum of a subtree is the sum of all the node values in that subtree, including its root.

Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": {
        "value": 3,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = [2, 3, 6].
1st example

Since all the sum values in this tree occur only once, return all of them in ascending order.

For
t = {
    "value": -2,
    "left": {
        "value": -3,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = [-3].
2nd example

There are 3 subtree sums for this tree: -2 + (-3) + 2 = -3, -3, and -2. The most frequent sum is -3 since it appears twice.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 105,
-20000 ≤ node value ≤ 20000.

[output] array.integer

The most frequent subtree sum. If there are several such sums, return them sorted in ascending order.
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
    return tree

from collections import defaultdict
def solution(t):
    m = defaultdict(int)
    
    def trav(t):
        nonlocal m
        if t:
            l = trav(t.left)
            r = trav(t.right)
            m[l+r+t.value] += 1
            return l + r + t.value
        else:
            return 0

    trav(t)

    for k in m.keys():
        if m[k] > 1:
            return [sorted(m.items(), key=lambda x:x[1], reverse=True)[0][0]]
    else:
        return sorted(m.keys())


t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 3,
        "left": None,
        "right": None
    }
}
print(solution(map_to_Tree(t))) # [2, 3, 6]

t = {
    "value": -2,
    "left": {
        "value": -3,
        "left": None,
        "right": None
    },
    "right": {
        "value": 2,
        "left": None,
        "right": None
    }
}

print(solution(map_to_Tree(t))) # [-3]

print(solution(map_to_Tree({"value":1,"left":None,"right":None}))) # ?

'''
# silverslash's solution

sums = {}

def solution(t):
    get_freqs(t)
    mf = max(sums.values()) if sums else -1
    return sorted(v for v, f in sums.items() if f == mf) if sums else []
    
def get_freqs(t):
    if t is None: return 0
    s = get_freqs(t.left) + get_freqs(t.right) + t.value
    sums[s] = sums[s] + 1 if s in sums else 1
    return s
'''