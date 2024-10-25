class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        else:
            for i in range(len(s)):
                if s[i:] + s[:i] == goal:
                    return True
            return False


so1 = Solution()
so1.rotateString("abcde", "cdeab")