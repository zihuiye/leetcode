#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            both_none = root.left is None and root.right is None
            value_same = root.left is not None and root.right \
                is not None and root.left.val == root.right.val

            if both_none:
                return True
            elif value_same:
                center_root = TreeNode(0)
                center_root.left = root.left.right
                center_root.right = root.right.left
                outer_root = TreeNode(0)
                outer_root.left = root.left.left
                outer_root.right = root.right.right
                return self.isSymmetric(center_root) and self.isSymmetric(outer_root)
            else:
                return False
            
# @lc code=end

