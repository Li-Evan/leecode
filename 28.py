'''
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。
'''

# KMP算法！！！！！！

def get_next(needle):
    next = [-1]
    i = 0
    j = next[i]
    while i < len(needle) - 1:
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1 # 最长前后缀相等+1
            next.append(j)
        else:
            j = next[j]
    return next

def kmp(haystack,needle):
    if needle == '':
        return 0
    next = get_next(needle)
    i = 0
    j = 0
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j >= len(needle):
        return i - len(needle)
    else:
        return -1



# 暴力解,超出时间限制
# def strStr(haystack: str, needle: str) -> int:
#     len_haystack = len(haystack)
#     len_needle = len(needle)
#     neddle1, neddle2 = 0, 0
#     count = 0
#
#     if needle == '':
#         return 0
#
#     if len_needle > len_haystack:
#         return -1
#
#     while neddle1 < len_haystack and neddle2 < len_needle:
#         for each in needle:
#             if each == haystack[neddle1]:
#                 neddle2 += 1
#                 neddle1 += 1
#                 if neddle1 >= len_haystack or neddle2 >= len_needle:
#                     break
#             else:
#                 count += 1
#                 neddle1 = count
#                 neddle2 = 0
#                 break
#
#     if neddle2 == len(needle):
#         return count
#     else:
#         return -1

# 暴力解的一种更简洁写法
# def strStr(self, haystack: str, needle: str) -> int:
#     """
#     :type S: str
#     :type T: str
#     :rtype: int
#     """
#     i = 0
#     j = 0
#     while i < len(haystack) and j < len(needle):
#         if haystack[i] == needle[j]:  # 依次比较，相等则比较下一个字符
#             i += 1
#             j += 1
#         else:  # 如果不相等，指针i需要回溯到上个起点的下一个位置
#             # 并从头开始比较
#             i -= j - 1
#             j = 0
#     # while循环结束后，要么是找到合适匹配了，要么是遍历完主串都没有找到合适匹配
#     if j == len(needle):
#         return i - j
#     else:
#         return -1