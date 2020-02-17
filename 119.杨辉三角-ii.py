#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0:
        #     return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        last_level = self.getRow(rowIndex-1)
        this_level = [last_level[i]+last_level[i+1] for i in range(len(last_level)-1)]
        this_level = [1] + this_level + [1]
        return this_level
# @lc code=end

