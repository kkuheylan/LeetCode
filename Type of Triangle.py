class Solution:
    def triangleType(self, nums):
        ns = set(nums)
        l = len(ns)
        a, b, c = nums[0], nums[1], nums[2]
        if not (a < b + c and b < a + c and c < b + a) :
            return "none"
        if l == 2 :
            return "isosceles"
        if l == 1 :
            return "equilateral"
        return "scalene"