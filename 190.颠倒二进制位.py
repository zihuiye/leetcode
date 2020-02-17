#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        b = str(bin(n))[2:]
        if len(b) < 32:
            b = ''.join(['0']*(32-len(b)))+b
        return int(b[::-1],2)
# @lc code=end

