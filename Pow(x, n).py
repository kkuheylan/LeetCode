class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x > 100.0 or x < -100.0:
            raise "x cannot be greater than 100 or less than - 100"
        return float(pow(x,n))