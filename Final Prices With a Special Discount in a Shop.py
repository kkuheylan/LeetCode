class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for left in range(len(prices)):
            for right in range(left+1, len(prices)):
                if prices[right] <= prices[left]:
                    prices[left] -= prices[right]
                    break
        return prices
    