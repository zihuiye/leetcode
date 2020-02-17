#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = None
        while True:
            if head is None:
                return root
            if root == None:
                root = now = ListNode(head.val)
            else:
                if head.val != now.val:
                    now.next = ListNode(head.val)
                    now = now.next
            head = head.next
            
            
# @lc code=end

