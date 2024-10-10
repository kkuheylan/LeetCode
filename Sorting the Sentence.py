class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_dict = {}
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.split(" ")
        result = []
        for i in s:

            for check_num in range(len(i)):
                print(i[check_num])
                if i[check_num] in nums:
                    num = i[check_num]
                    word = i[:-1]
                    my_dict[int(num)] = word
                    break
        for k in range(1, len(my_dict) + 1):
            result.append(my_dict[k])   
        
        return " ".join(result)
            
                    
                



so1 = Solution()
so1.sortSentence("is2 sentence4 This1 a3")