#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                p = i+1
                continue
            elif nums[i] > target:
                return p
        return len(nums)

# @lc code=end

