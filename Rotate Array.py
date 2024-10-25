class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        first_shape = []
        second_shape = []
        first_shape = nums[size-k:]
        second_shape = nums[:size-k]
        nums[:] = first_shape + second_shape
        return nums
    
    
so1 = Solution()
print(so1.rotate([1,2,3,4,5,6,7], 3))