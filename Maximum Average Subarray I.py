class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # İlk pencereyi oluşturuyoruz ve toplamı hesaplıyoruz
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Kayan pencereyi kaydırarak en büyük toplamı buluyoruz
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Ortalamayı float olarak döndürüyoruz
        # print(max_sum / float(k))
        return max_sum / float(k)


so1 = Solution()
so1.findMaxAverage([1, 12, -5, -6, 50, 3], 4)   # 12.75
