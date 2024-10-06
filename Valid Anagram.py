
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s.lower()
        t.lower()
        if len(s) != len(t):
            return False
        s_list = []
        t_list = []
        for i_s in s:
            s_list.append(i_s)
        for i_t in t:
            t_list.append(i_t)
        s_list.sort()
        t_list.sort()
    
        if s_list == t_list:
            return True
        else:
            return False