#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            center = (len(nums)-1)//2
            root = TreeNode(nums[center])
            root.left = self.sortedArrayToBST(nums[:center])
            root.right = self.sortedArrayToBST(nums[center+1:])
            return root
# @lc code=end

