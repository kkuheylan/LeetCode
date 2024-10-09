

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 1
        values = []
        while right == len(s):
            res = s[left:right]
            values.append(res)
            left += 1
            right += 1
            print(left)
            print(right)
        print(values)

so1 = Solution()
so1.lengthOfLongestSubstring([1,2,3,4,5,6,7,8])