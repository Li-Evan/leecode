''''''
'''
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
'''

# class Solution:
#     def partition(self,nums,left,right):
#         temp = nums[left]
#         while left < right:
#             while left < right and nums[right] >= temp:
#                 right -= 1
#             nums[left] = nums[right]
#             while left < right and nums[left] <= temp:
#                 left += 1
#             nums[right] = nums[left]
#         nums[left] = temp
#         return left
#     def quick_sort(self,nums,left,right):
#         if left< right:
#             mid = self.partition(nums,left,right)
#             self.quick_sort(nums,left,mid-1)
#             self.quick_sort(nums,mid+1,right)
#         return nums
#     def thirdMax(self, nums) -> int:
#         if len(nums) < 3:
#             return max(nums)
#         new_li = []
#         for i in nums:
#              if i not in new_li:
#                  new_li.append(i)
#         if len(new_li) < 3:
#             return max(new_li)
#         if len(new_li) == 3:
#             return min(new_li)
#
#         sort_li = self.quick_sort(new_li,0,len(new_li)-1)
#         return sort_li[-3]

# def thirdMax(nums):
#     count = 0
#     li = []
#     while count < 3 or len(nums) != 0:
#         print(len(nums))
#         print(nums)
#         li.append(max(nums))
#         nums.remove(max(nums))
#         count += 1
#     if len(li) < 3:
#         return max(li)
#     else:
#         return min(li)

