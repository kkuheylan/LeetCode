class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        line = 1
        index = 0
        values = []
        size = 0
        for i in range(len(triangle)):
            size += len(triangle[i])
        values.append(triangle[0][0])
        