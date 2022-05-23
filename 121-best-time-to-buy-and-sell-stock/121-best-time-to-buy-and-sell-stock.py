class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxprofit = 0
        while right < len(prices):
            current = prices[right]-prices[left]
            if prices[left]<prices[right]:
                maxprofit = max(maxprofit,current)
            else:
                left = right
            right += 1
        return maxprofit
            