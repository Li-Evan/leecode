''''''
'''给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 '''

class Solution:
    def maxSubArray(self, nums) -> int:
        ans = nums[0]
        sum = nums[0]
        for i in range(1,len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            ans = max(ans,sum)
        return ans