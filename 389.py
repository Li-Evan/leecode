''''''
'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic = {}
        t_dic = {}
        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 0

        for j in t:
            if j in t_dic:
                s_dic[j] += 1
            else:
                s_dic[j] = 0

        for i in t_dic.keys():
            if i in s_dic.keys():
                if t_dic[i] != s_dic[i]:
                    return i
            else:
                return i
