#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = now = ListNode(0)
        p = 0
        while True:
            v = 0
            if l1 is not None:
                v += l1.val
            if l2 is not None:
                v += l2.val
            if p>0:
                v += 1
                p = 0
            if v >= 10:
                v = v-10
                p = 1
            now.val = v
            # print(root, now, l1, l2)
            
            if (l1 and l1.next) or (l2 and l2.next) or p > 0:
                now.next = ListNode(0)
                now = now.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            else:
                return root

