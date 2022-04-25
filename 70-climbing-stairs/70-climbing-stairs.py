class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]*n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        result[0] = 1
        result[1] = 2
        for i in range(2,n):
            result[i] += result[i-1]+result[i-2]
        return result[n-1]