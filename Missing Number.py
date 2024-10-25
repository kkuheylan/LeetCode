class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = []
        for i in nums:
            if i not in values:
                values.append(i)
        for i in range(len(values)+1):
            if i not in nums:
                return i