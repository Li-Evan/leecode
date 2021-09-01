''''''
'''
349
给定两个数组，编写一个函数来计算它们的交集。
'''

# class Solution:
#     def intersection(self, nums1, nums2) :
#         dic = {}
#         li = []
#         nums1 = set(nums1)
#         nums2 = set(nums2)
#         for i in nums1:
#             dic[i] = 1
#         for j in nums2:
#             if j in dic.keys():
#                 li.append(j)
#         return li


'''350'''

class Solution:
    def intersect(self, nums1, nums2) :
        dic = {}
        li = []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in nums2:
            if j in dic.keys() and dic[j] != 0:
                li.append(j)
                dic[j] -= 1
        return li



















