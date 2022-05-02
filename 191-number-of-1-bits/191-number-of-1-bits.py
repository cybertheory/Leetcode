class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in bin(n).replace("0b",""):
            if int(i) == 1:
                count += 1
        return count