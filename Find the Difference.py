class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_asci_sum = (sum(ord(x) for x in s))
        t_asci_sum = (sum(ord(y) for y in t))
        return (chr(abs(t_asci_sum-s_asci_sum)))