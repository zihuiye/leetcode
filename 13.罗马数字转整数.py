#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 1:
            return r[s]
        ssum = 0
        for i,c in enumerate(s):
            if i < (len(s)-1):
                isfn = c == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')
                isfnz = c == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')
                isfnzz = c == 'C' and (s[i+1] == 'D' or s[i+1] == 'M')
            else:
                isfn = isfnz = isfnzz = False
            if isfn or isfnz or isfnzz:
                ssum -= r[c]
            else:
                ssum += r[c]
        return ssum



