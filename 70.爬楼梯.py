#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            i = 2
            while i<n:
                a, b = b, a+b
                i += 1
            return b
               
# @lc code=end

