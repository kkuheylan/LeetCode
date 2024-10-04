class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        base = len(min(strs))
        array_length = len(strs)
        x = 0
        for i in range(base):
            for x in range(array_length):
                if 