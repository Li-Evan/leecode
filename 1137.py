''''''
'''
泰波那契序列Tn定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数n，请返回第 n 个泰波那契数Tn 的值。


'''

class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        if n > 2:
            while len(tri) <= n:
                tri.append(tri[-3]+tri[-2]+tri[-1])
        return tri[n]