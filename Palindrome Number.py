class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        result = []
        
        def split(n):
            return [int(i) for i in str(n)]

        result = split(x)

        if len(result) % 2 == 0:
            double_num = []
            check_dou = []

            for i in range(len(result)//2):
                double_num.append(result.pop())

            for k in range(len(result)):
                check_dou.append(result[k])

            if check_dou == double_num[::-1]: 
                return True
            else:
                return False

        else:
            single_num = []
            check_res = [] 

            middle = len(result) // 2
            result.pop(middle)

            for i in range(len(result)//2):
                single_num.append(result.pop()) 

            for k in range(len(result)):
                check_res.append(result[k])

            if check_res == single_num[::-1]: 
                return True
            else:
                return False
