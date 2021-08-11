''''''
'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

'''
#
# class Solution:
#     def intToRoman(self,num: int):
#         li = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#         li1 = []
#         count = 12
#         while count >= 0:
#             li1.append(num // li[count])
#             num %= li[count]
#             count -= 1
#         # li1.reverse()
#         print(li1)
#         str_result = 'M' * li1[0] + 'CM' * li1[1] + 'D' * li1[2] + 'CD' * li1[3] + 'C' * li1[4] + 'XC' * li1[5] + 'L' * \
#                      li1[6] + 'XL' * li1[7] + 'X' * li1[8] + 'IX' * li1[9] + 'V' * li1[10] + 'IV' * li1[11] + 'I' * li1[12]
#         return str_result

# class Solution:
#     def intToRoman(self,num: int):
#         dic = {}
#         li = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#         li2 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#         count = 12
#         count2 = 0
#         while count >= 0:
#             dic[li2[count2]] = num // li[count]
#             num %= li[count]
#             count -= 1
#             count2 += 1
#         str_result = ''
#         for k in dic:
#             str_result += k*dic[k]
#
#         return str_result

# 来源：leecode题解 非自己写
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         M = ["", "M", "MM", "MMM"] # 1000，2000，3000
#         C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100~900
#         X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
#         I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
#         return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]


def intToRoman(num: int):
    dic = {}
    li = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    li2 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    count = 12
    count2 = 0
    while count >= 0:
        dic[li2[count2]] = num // li[count]
        num %= li[count]
        count -= 1
        count2 += 1
    print(dic)
    str_result = ''
    for k in dic:
        str_result += k*dic[k]

    return str_result

print(intToRoman(3))

# def intToRoman(num: int):
#     li = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#     li1 = []
#     count = 12
#     while count >= 0:
#         li1.append(num // li[count])
#         num %= li[count]
#         count -= 1
#     # li1.reverse()
#     print(li1)
#     str_result = 'M'*li1[0]+'CM'*li1[1]+'D'*li1[2]+'CD'*li1[3]+'C'*li1[4]+'XC'*li1[5]+'L'*li1[6]+'XL'*li1[7]+'X'*li1[8]+'IX'*li1[9]+'V'*li1[10]+'IV'*li1[11]+'I'*li1[12]
#     return str_result
#
# print(intToRoman(1994))








