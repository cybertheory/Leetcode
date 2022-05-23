class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = set()
        for n in nums:
            if n in table:
                return True
            table.add(n)
        return False
        