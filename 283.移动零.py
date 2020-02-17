#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if nums[i] == 0:
                print(nums[len(nums)-p:i-1:-1])
                
                nums[i:len(nums)-p] = nums[len(nums)-p:i-1:-1]
                # print(nums)
                # print(nums[len(nums)-p-2:i-1:-1])
                nums[i:len(nums)-p-1] = nums[len(nums)-p-2:i-1:-1]

                # print(nums[i:len(nums)-p-1])
                p += 1
        # print(nums)
# @lc code=end

