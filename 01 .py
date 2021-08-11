'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，
并返回它们的数组下标。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 3544 ms
# def sum_in(nums,target):
#     answ_li = []
#     for i in range(len(nums)):
#         for j in range(i + 1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 answ_li.append(i)
#                 answ_li.append(j)
#                 break
#     return answ_li

# 1988 ms
# def sum_in(nums,target):
#     answ_li = []
#     for i in range(len(nums)):
#         j_target = target - nums[i]
#         for j in range(i+1,len(nums)):
#             if nums[j] == j_target:
#                 answ_li.append(i)
#                 answ_li.append(j)
#     return answ_li

# 40ms
def sum_in(nums,target):
    hash_dic = {}
    for index, num in enumerate(nums):
        hash_dic[num] = index
    for index,num in enumerate(nums):
        j_target = target - num
        if j_target in hash_dic and hash_dic[j_target] != index:
            return [index, hash_dic[j_target]]
    return []


