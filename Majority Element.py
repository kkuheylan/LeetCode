class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if i > len(nums)/2:
                
                return i
so1 = Solution()
so1.majorityElement([3,2,3])