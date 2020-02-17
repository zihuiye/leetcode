#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return
        i = 0
        j = 0    
        while i + j  < m + n :
            print(nums1, i, j)
            if i == m:
                nums1[i+j] = nums2[j]
                j += 1
            elif j < n and nums1[j+i] > nums2[j]:
                nums1[j+i+1:j+m+1] = nums1[j+i:m+j]
                nums1[i+j] = nums2[j]
                j += 1
            else:
                i += 1
# @lc code=end

