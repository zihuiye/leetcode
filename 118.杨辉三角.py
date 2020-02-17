#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return self.generate(1)+[[1,1]]
        last_tri = self.generate(numRows-1)
        last_level = last_tri[-1]
        this_level = [last_level[i]+last_level[i+1] for i in range(len(last_level)-1)]
        this_level = [1] + this_level + [1]
        return last_tri + [this_level]
# @lc code=end

