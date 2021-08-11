''''''
'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
'''

# class Solution:
#     def isPalindrome(self,x: int) -> bool:
#         if x < 0 or x % 10 == 0:
#             return False
#         x = str(x)
#         li = []
#         for each in x:
#             li.append(each)
#         for i in range(len(li) // 2):
#             if li[i] != li[-(i + 1)]:
#                 return False
#         return True

# class Solution:
#     def isPalindrome(self,x: int) -> bool:
#         if x < 0:
#             return False
#         x1 = x
#         x2 = x
#         y = 0
#         count = 1
#         while x // 10 != 0:
#             count *= 10
#             x //= 10
#
#         while count > 1:
#             y += (x1 % 10) * count
#             x1 //= 10
#             count //= 10
#
#         y += x * count
#
#         if y == x2:
#             return True
#         else:
#             return False

class Solution:
    def isPalindrome(self,x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        x = str(x)

        y = ''.join(reversed(x))
        ''' 字符串可以直接这样进行翻转！！！！！不用通过列表！！！！！'''

        if x == y:
            return True
        else:
            return False

# def isPalindrome(x: int) -> bool:
#     if x < 0:
#         return False
#     x1 = x
#     x2 = x
#     y = 0
#     count = 1
#     while x // 10 != 0:
#         count *= 10
#         x //= 10
#         # y += (x % 10) * count
#         # x //= 10
#         # if y != 0:
#         #    count *= 10
#     while count > 1:
#         y += (x1 % 10) * count
#         x1 //= 10
#         count //= 10
#
#     y += x * count
#
#     if y == x2:
#         return True
#     else:
#         return False
# print(isPalindrome(121))