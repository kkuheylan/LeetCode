class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        show_s = s.index(c)
        values = []
        for i in range(len(s)):
            if s[i] == c:
                show_s = i
            values.append(abs(i - show_s))
        return values
        

so1 = Solution()
so1.shortestToChar("loveleetcode", "e")

#Link: https://leetcode.com/problems/shortest-distance-to-a-character/
#unfortunately, this solution is not working for all test cases.