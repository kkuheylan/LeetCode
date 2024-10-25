class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        for i in nums:
            if i*2 > max_num and i != max_num:
                return -1
                break
        return nums.index(max_num)
    
# TIME: O(N)
# SPACE: O(1)
# SUCCESSFUL