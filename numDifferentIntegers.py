class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        alfabe = "abcdefghijklmnopqrstuvwxyz"
        for i in alfabe:
            word = word.replace(i," ")
        num = word.split(" ")
        word = word.split()
        list_for_word_len = []
        for k in word:
            if k not in list_for_word_len:
                list_for_word_len.append(k)
        int_nums = set()
        for zero_del in list_for_word_len:
            int_nums.add(str(int(zero_del)))
            
        return len(int_nums)

        
so1 = Solution()
so1.numDifferentIntegers("a1b01c001")