class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            target_index = nums.index(target)
            return target_index
        else:
            nums.append(target)
            nums.sort()
            target_index = nums.index(target)
            return target_index