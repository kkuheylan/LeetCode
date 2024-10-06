class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in nums:
            num_count = nums.count(i)
            if num_count == 1:
                result.append(i)
        return sum(result)