#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(i) for i in list(str(bin(n)))])
        # return sum(str(bin(s&n)).split())
# @lc code=end

