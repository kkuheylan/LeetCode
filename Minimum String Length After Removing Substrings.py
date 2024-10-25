from re import L
import re


class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[left:right] == "AB" or s[left:right] == "BA":
                    s = s[:left] + s[right:]
                    left += 1
                    right += 1
        print(s)
        return len(s)
    
so1 = Solution()
so1.minLength("CABABD") # 2