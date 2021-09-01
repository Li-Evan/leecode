''''''
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        li = [0,1,2]
        for i in range(n-2):
            x = li[-2] + li[-1]
            li.append(x)
        return li[n]