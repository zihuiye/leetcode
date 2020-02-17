#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) == 0:
            return -1
        p = 0
        while True:
            if len(haystack) - p < len(needle):
                break
            if haystack[p] == needle[0]:
                i = 1
                while True:
                    if len(needle) == i:
                        return p
                    if haystack[p+i] != needle[i]:
                        break
                    i = i + 1
            p = p + 1
        return -1
# @lc code=end

