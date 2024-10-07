class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_count = 0
        white_count=0
        blue_count = 0
        result = []
        for num in nums:
            if num == 0:
                red_count += 1
            elif num == 1:
                white_count += 1
            else:
                blue_count += 1
                
        for red in range(red_count):
            result.append(0)
        for white in range(white_count):
            result.append(1)
        for blue in range(blue_count):
            result.append(2)
        return result