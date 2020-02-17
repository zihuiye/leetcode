#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        if not strs:
            return s
        for i,c in enumerate(strs[0]):
            try:
                if False not in map(lambda x: x[i]==c, strs):
                    s += c
                else:
                    break
            except:
                return s
        return s

