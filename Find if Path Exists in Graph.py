class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        
        if left < ranges[0][0] or left > ranges[-1][-1] or right > [-1][-1] or right > [0][0]:
            return False
        else:
            return True