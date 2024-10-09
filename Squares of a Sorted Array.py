from math import pow


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            result.append(int(pow(i,2)))
        result.sort()   
        return result