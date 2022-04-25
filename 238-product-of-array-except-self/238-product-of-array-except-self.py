import math
from itertools import chain
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        left_sum = 1
        right_sum = 1
        l,r  = 0,len(nums)-1
        
        while l < len(nums) and r >= 0:
            res[l] *= left_sum
            left_sum *= nums[l]
            res[r] *= right_sum
            right_sum *= nums[r]
            
            l += 1
            r -= 1
        
        return res
                
            