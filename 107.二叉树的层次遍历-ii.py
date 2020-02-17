#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        is_leaf = root.left is None and root.right is None
        if is_leaf:
            return [[root.val]]
        elif root.left and root.right is None:
            left_list = self.levelOrderBottom(root.left)
            return left_list + [[root.val]]
        elif root.left is None and root.right:
            right_list = self.levelOrderBottom(root.right)
            return right_list + [[root.val]]
        else:
            left_list = self.levelOrderBottom(root.left)
            right_list = self.levelOrderBottom(root.right)
            # print(left_list,right_list)

            combine = list()
            for ls in range(1,1+max(len(left_list),len(right_list))):
                right = right_list[-ls] if ls <= len(right_list) else []
                left = left_list[-ls] if ls <= len(left_list) else []
                combine.append(left+right)
            combine.reverse()
            return combine + [[root.val]]

            
# @lc code=end

