'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Input: nums = [1,3]
Output: [3,1]

Constraints:
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in a strictly increasing order.
'''

from typing import Optional, List
from TreeNodeUtil import TreeNode, convertBfsList

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        print(mid, nums[mid], nums)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

nums1 = [-10,-3,0,5,9]
nums2 = [1,3]

s = Solution()

print(convertBfsList(s.sortedArrayToBST(nums1)))
print(convertBfsList(s.sortedArrayToBST(nums2)))