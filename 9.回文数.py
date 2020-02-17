#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0 :
            return True
        s = str(x)[::-1]
        if s == str(x):
            return True
        else:
            return False


