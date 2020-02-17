#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        half_n = int(n/2)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[:half_n])
            max_right = self.maxSubArray(nums[half_n:])
        print('nums:',nums)
        print('max_l,max_r',nums[:half_n],nums[half_n:])
        left_sums = [sum(nums[i:half_n]) for i in range(half_n)]
        right_sums = [sum(nums[half_n:i+1]) for i in range(half_n,n)]
        print(left_sums,right_sums)
        return max(max_left, max_right, max(left_sums)+max(right_sums))
# @lc code=end

