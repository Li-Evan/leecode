''''''
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
'''

class Solution:
    def maxArea(self, height):
        longest_j = height[-1]
        longest_i = height[0]
        n = len(height)
        max_area = n * min(longest_i,longest_j)
        for i in range(n-1):
            if height[i] >= longest_i:
                for j in range(i+1,n):
                    if height[j] >= longest_j:
                        if (j-i)*min(height[i],height[j]) > max_area:
                            max_area = (j-i) * min(height[i],height[j])
        return max_area