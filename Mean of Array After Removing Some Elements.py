class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        arr_length = len(arr)
        del_nums_length = int((arr_length * 5) / 100)
        
        trimmed_arr = arr[del_nums_length: -del_nums_length]        
        return sum(trimmed_arr) / float(len(trimmed_arr))