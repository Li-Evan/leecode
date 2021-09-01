''''''
'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        for j in t:
            if j not in dic.keys():
                return False
            else:
                dic[j] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True