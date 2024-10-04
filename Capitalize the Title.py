class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        split_result = title.split()  
        for i in range(len(split_result)):
            if len(split_result[i]) > 2:
                split_result[i] = split_result[i].capitalize()
            else:
                split_result[i] = split_result[i].lower()
        split_result = ' '.join([str(i) for i in split_result])
        print(split_result)
    



so1 = Solution()
so1.capitalizeTitle("capiTalIze tHe titLe")

