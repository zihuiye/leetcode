#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
        elif root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        elif root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
# @lc code=end

