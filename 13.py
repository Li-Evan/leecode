''''''
'''
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# def romanToInt(s: str) -> int:
#     num_result = 0
#     dic1 = {
#         'CM': 900,
#         'CD': 400,
#         'XC': 90,
#         'XL': 40,
#         'IX': 9,
#         'IV': 4,
#     }
#     dic2 = {
#         'M': 1000,
#         'D': 500,
#         'C': 100,
#         'L': 50,
#         'X': 10,
#         'V': 5,
#         'I': 1,
#     }
#
#     needle = 0
#     length = len(s)
#     while needle + 2 <= length:
#         print(num_result)
#         if s[needle] in ['I', 'X', 'C']:
#             x = s[needle:needle + 2]
#             if x in dic1:
#                 num_result += dic1[x]
#                 needle += 2
#             else:
#                 num_result += dic2[x[0]]
#                 needle += 1
#         else:
#             num_result += dic2[s[needle]]
#             needle += 1
#     if needle != length:
#         num_result += dic2[s[-1]]
#     return num_result
#
# print(romanToInt("MDCCCLXXXIV"))

def romanToInt(s: str) -> int:
    num_result = 0
    dic = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }

    needle = 0
    while needle+1 < len(s):
        print(num_result)
        if dic[s[needle]] >= dic[s[needle+1]]:
            num_result += dic[s[needle]]
        else:
            num_result -= dic[s[needle]]
        needle += 1
    num_result += dic[s[needle]]
    return num_result

print(romanToInt("MDCCCLXXXIV"))