#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        while True:
            if not l1 and not l2:
                return result
            elif l1 and not l2:
                new_node = ListNode(l1.val)
                l1 = l1.next
            elif not l1 and l2:
                new_node = ListNode(l2.val)
                l2 = l2.next
            else:
                if l1.val > l2.val:
                    new_node = ListNode(l2.val)
                    l2 = l2.next
                else:
                    new_node = ListNode(l1.val)
                    l1 = l1.next
            if not result:
                result = current = new_node
            else:
                current.next = new_node
                current = current.next
# @lc code=end

