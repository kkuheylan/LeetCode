class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        ayir = len(nums)/2
        for i in range(ayir):
            result.append(nums[0+i])
            if i == ayir:
                result.append(nums[n+i]-1)
            else:
                result.append(nums[n+i])
        return result