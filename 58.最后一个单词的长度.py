#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i,c in enumerate(s):
            if c != " ":
                l += 1
            elif i < len(s) - 1 and s[i+1] != " ":
                l = 0
        return l
# @lc code=end

