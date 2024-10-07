class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        move_values = []
        lenght_nums = len(nums)
        if (len(nums)%2==0):
             median_n = int((nums[int(lenght_nums/2)-1] + nums[int(lenght_nums/2)])/2)
        else:
            median_n = nums[int(lenght_nums/2)]
        for gap in nums:
            count = 0
            count = count + abs(gap-median_n)
            move_values.append(count)
        return (sum(move_values))
    
so1 = Solution()
so1.minMoves2([1,3,2])