''''''
'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，
这样它就有足够的空间保存来自 nums2 的元素。

'''
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ltmp = []
        needle1 = 0
        needle2 = 0
        while needle1 <= m-1 and needle2 <= n-1:
            if nums1[needle1] < nums2[needle2]:
                ltmp.append(nums1[needle1])
                needle1 += 1
            else:
                ltmp.append(nums2[needle2])
                needle2 += 1
        while needle1 <= m-1:
            ltmp.append(nums1[needle1])
            needle1 += 1
        while needle2 <= n-1:
            ltmp.append(nums2[needle2])
            needle2 += 1

        nums1 = ltmp
