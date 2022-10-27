class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0
        left_p = 0
        right_p = 1
        while right_p < len(prices):
            profit = prices[right_p] - prices[left_p]
            if profit > 0:
                if profit>max_prof:
                    max_prof = profit
            else:
                left_p = right_p
            right_p += 1
        return max_prof