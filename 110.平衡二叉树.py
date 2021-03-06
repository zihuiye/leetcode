#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def isB(root):
            if not root:return True,0
            lb,ls = isB(root.left)
            rb,rs = isB(root.right)
            return lb and rb and abs(ls - rs) <= 1, max(ls, rs) + 1
        return isB(root)[0]
# @lc code=end

