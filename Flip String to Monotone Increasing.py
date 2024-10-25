
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        flips = 0
        for i in s:
            if i == '1':
                ones += 1
            else:
                flips = min(flips+1, ones)
        return flips

# TIME: O(N)
# SPACE: O(1)
# SUCCESSFUL