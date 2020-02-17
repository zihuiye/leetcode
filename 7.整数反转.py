#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        s = -1 if x < 0 else 1
        x *= s
        x = int(str(x)[::-1])
        x *= s
        if -2**31 <= x <= (2**31):
            return x
        else:
            return 0



