'''
2022/06/07

https://app.codesignal.com/interview-practice/task/FwAR7koSB3uYYsqDp/description

Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.

Example

For level = 3 and pos = 3, the output should be
solution(level, pos) = "Doctor".

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer level

The level of a person in the ancestor tree, 1-based.

Guaranteed constraints:
1 ≤ level ≤ 30.

[input] integer pos

The position of a person in the given level of ancestor tree, 1-based, counting from left to right.

Guaranteed constraints:
1 ≤ pos ≤ 2(level - 1).

[output] string

Return Engineer or Doctor.
'''
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def traversal_preorder(tree:Tree, result_list):
    if tree:
        result_list.append(tree.value)
        traversal_preorder(tree.left, result_list)
        traversal_preorder(tree.right, result_list)
    return result_list

# def solution(level, pos):

#     def create_tree(prof, level):
#         node = Tree(prof)
#         if level > 0:
#             if prof == "E":
#                 node.left = create_tree("E", level - 1)
#                 node.right = create_tree("D", level - 1)
#             elif prof == "D":
#                 node.left = create_tree("D", level - 1)
#                 node.right = create_tree("E", level - 1)
#             return node
#         else:
#             return None

#     tree = create_tree("E", level)

#     leaves = []
#     def get_leaves(tree):
#         if not tree:
#             return
        
#         if tree.left is None and tree.right is None:
#             leaves.append(tree.value)

#         get_leaves(tree.left)
#         get_leaves(tree.right)

#     get_leaves(tree)
#     return "Engineer" if leaves[pos - 1] == "E" else "Doctor"


def solution(level, pos):
    # ???
    return ["Engineer", "Doctor"][bin(pos - 1).count('1')%2]


print(solution(3,3)) # "Doctor"
