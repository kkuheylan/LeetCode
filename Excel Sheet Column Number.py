class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        line = 0
        columnTitle = columnTitle[::-1]
        if len(columnTitle) == 1:
            return ord(columnTitle) - 64
        for i in (columnTitle):
            if line == 0:
                result += ord(i) - 64
                line += 1
            else:
                result += (ord(i) - 64) * 26 ** line  
                line += 1
            # print(f"i: {i}, değerin ord: {ord(i) - 64} ve line: {line} ve result: {result}, value: {(ord(i)-64)* 26 ** line}")
        return result
            
so1 = Solution()
so1.titleToNumber("FXSHRXW")
                

# Time: O(n)
# Space: O(1)
