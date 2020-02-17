#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            diff = target - n
            l = nums[i+1:]
            if diff in l:
                return [i, 1+i+l.index(diff)]
        return None

