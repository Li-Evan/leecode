''''''
'''
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
'''

class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for i in nums:
            if i in dic.keys():
                return True
            else:
                dic[i] = 1

        return False