#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        else:
            for i in range(1,x+1):
                ss = i*i
                if ss == x:
                    return i
                elif ss>x :
                    return i-1
# @lc code=end

