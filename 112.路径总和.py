#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        is_leaf = not root.left and not root.right
        if sum == root.val and is_leaf:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        
# @lc code=end

