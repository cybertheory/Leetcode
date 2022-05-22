class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for n in range(len(nums)):
            find = target-nums[n]
            if find in lookup:
                return [lookup[find],n]
            lookup[nums[n]] = n
        return []