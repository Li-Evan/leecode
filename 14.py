''''''
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# class Solution:
#     def longestCommonPrefix(self, strs) :
#         shortest_loc = 0
#         for i in range(len(strs)):
#             if len(strs[i]) < len(strs[shortest_loc]):
#                 shortest_loc = i
#         count = 0
#         while True:
#             if count < len(strs[shortest_loc]):
#                 flag = strs[shortest_loc][count]
#                 for i in range(len(strs)):
#                     if strs[i][count] != flag and i != shortest_loc:
#                         return strs[shortest_loc][:count]
#                 count += 1
#             else:
#                 return strs[shortest_loc]


class Solution:
    def twolongest(self,str1, str2):
        if len(str1) < len(str2):
            short = str1
            long = str2
        else:
            short = str2
            long = str1

        for i in range(len(short)):
            if short[i] != long[i]:
                return short[:i]
        return short

    def longestCommonPrefix(self, strs) :
        longestcommon = strs[0]
        str1_loc = 0
        while str1_loc <= len(strs) - 2:
            x = self.twolongest(strs[str1_loc],strs[str1_loc+1])
            if not x:
                return ""
            else:
                if len(x) < len(longestcommon):
                    longestcommon = x
                str1_loc += 1
                continue
        return longestcommon












