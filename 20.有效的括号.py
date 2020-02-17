#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        start = ('(','{','[')
        end = (')','}',']')
        i = 0
        l = list(s)
        while True:
            if l == []:
                break
            if i > len(l) - 1:
                valid = False
                break
            if l[i] in start:
                i += 1
                continue
            if l[i] in end:
                if i - 1 < 0:
                    valid = False
                    break
                if end.index(l[i]) == start.index(l[i-1]):
                    # print(i,l)
                    l = l[:i-1] + l[i+1:]
                    i -= 1
                    continue
                else:
                    valid = False
                    break
            
        return valid


