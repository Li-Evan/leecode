''''''
'''
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
'''

# def partition(li,left,right):
#     temp = li[left]
#     while left < right:
#         while left < right and li[right] >= temp:
#             right -= 1
#         li[left] = li[right]
#         while left < right and li[left] <= temp:
#             left += 1
#         li[right] = li[left]
#
#     li[left] = temp
#     return left
#
# def qucik_sort(li,left,right):
#     if left < right:
#         mid = partition(li,left,right)
#         qucik_sort(li,left,mid-1)
#         qucik_sort(li,mid+1,right)
#
# class Solution:
#     def missingNumber(self, nums) -> int:
#         sort_li = self.qucik_sort(nums,0,len(nums)-1)
#         for index,val in enumerate(sort_li):
#             if sort_li[index] != val:
#                 return index
#
#     def partition(self,nums, left, right):
#         temp = nums[left]
#         while left < right:
#             while left < right and nums[right] >= temp:
#                 right -= 1
#             nums[left] = nums[right]
#             while left < right and nums[left] <= temp:
#                 left += 1
#             nums[right] = nums[left]
#
#         nums[left] = temp
#         return left
#
#     def qucik_sort(self,nums, left, right):
#         if left < right:
#             mid = partition(nums, left, right)
#             qucik_sort(nums, left, mid - 1)
#             qucik_sort(nums, mid + 1, right)
#         return nums





# class Solution:
#     def missingNumber(self, nums) -> int:
#         dic = {}
#         for i in nums:
#             dic[i] = i
#
#         for i in range(len(nums)+1):
#             if i not in dic.keys():
#                 return i




class Solution:
    def missingNumber(self, nums) -> int:
        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        no_miss_sum = ((1+n)*n)/2
        return int(no_miss_sum - sum)

