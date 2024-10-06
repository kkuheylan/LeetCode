class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1): #diziyi tersten oku
            if digits[i] == 9: #sayı 9 ise 0 yap
                digits[i] = 0
            else: # değilse +1 ekle
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits #dizinin tamımı 9 ise baştakini 9 gerisini 0 yap
