'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 28 ms
# def solute(nums):
#     i = 1
#     for each in nums:
#         if each != nums[i-1]:
#             nums[i] = each
#             i += 1
#     return nums[:i],i
#
#
# print(solute([0,0,1,1,1,2,2,3,3,4]))

'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
nums = [1,1,1,2,2,3] k = 2
'''

# def solute(nums):
#     i = 2
#     if len(nums) <= 2:
#         return len(nums)
#     for j in range(2, len(nums)):
#         if nums[j] != nums[i - 2]:
#             nums[i] = nums[j]
#             i += 1
#     return i
#
# print(solute([0,0,1,1,1,1,2,3,3]))

# def solute(nums,k=2):
#     i = 0
#     for each in nums:
#         if i < k or nums[i-k] != each:
#             nums[i] = each
#             i += 1
#     return i


