#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        say = '1'
        i = 1
        while True:
            if i == n:
                return say
            newsay = ''
            for j,s in enumerate(say):
                # print(j,s,i)
                if j == 0:
                    current = s
                    c_n = 1
                elif j < len(say)-1:
                    if say[j] == current:
                        c_n += 1
                    else:
                        newsay+=str(c_n)+str(current)
                        current = s
                        c_n = 1
                else:
                    if say[j] == current:
                        c_n += 1
                        newsay += str(c_n)+str(s)
                    else:
                        newsay+=str(c_n)+str(current)+'1'+str(s)
                # print(newsay)
            if say == '1':
                newsay = '11'
            say = newsay
            # print('say:'+say)
            i += 1
            
# @lc code=end

