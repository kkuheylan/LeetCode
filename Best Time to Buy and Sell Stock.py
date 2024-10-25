class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0 
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price

        return max_profit

        
        
        
        
        
s1 = Solution()
s1.maxProfit([7,1,5,3,6,4])