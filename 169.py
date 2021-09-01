''''''
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

'''

# class Solution:
#     def majorityElement(self, nums) -> int:
#         dic = {}
#         for i in nums:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
#         for j in dic:
#             if dic[j] > len(nums)/2:
#                 return j




class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        maj = nums[0]
        for i in nums:
            if count == 0:
                maj = nums[i]
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
        return maj