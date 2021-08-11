'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# class Solution:
#     def reverse(self, x: int) -> int:
#         max = 2 ** 31 - 1
#         min = -2 ** 31
#         if -10 < x < 10:
#             return x
#
#         count = 0
#         if x < 0:
#             count = 1
#             x = abs(x)
#         x = str(x)
#         li1 = []
#         li2 = []
#         for each in x:
#             li1.append(each)
#         while li1[-1] == '0':
#             li1.pop()
#         while len(li1) > 0:
#             y = li1.pop()
#             li2.append(y)
#         m = ''.join(li2)
#         m = int(m)
#         if min <= m <= max:
#
#             if count == 0:
#                 return m
#             else:
#                 return -m
#         else:
#             return 0
#


# from functools import reduce
# class Solution:
#     def reverse(self, x: int) -> int:
#         max = 2 ** 31 - 1
#         min = -2 ** 31
#         if -10 < x < 10:
#             return x
#
#         count = 0
#         if x < 0:
#             count = 1
#             x = abs(x)
#         li = []
#         while x // 10 != 0:
#             li.append(x % 10)
#             x //= 10
#         li.append(x % 10)
#
#         while li[-1] == 0:
#             li.pop()
#         li.reverse()
#         new_x = reduce((lambda x,y : x*10 + y),li)
#         if min <= new_x <= max:
#             if count == 0:
#                 return new_x
#             else:
#                 return -new_x
#         return 0







# def reverse( x: int) -> int:
#     li = []
#     while x // 10 != 0:
#         li.append(x % 10)
#         x //= 10
#     li.append(x % 10)
