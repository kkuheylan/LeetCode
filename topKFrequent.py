class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            counter = nums.count(num)
            count[num] = counter
            
        count_values = count.values()   
        count_values.sort()
        # max_count_num = max(count.values())
        edited_count_values = []
        for i in count_values:
            if i not in edited_count_values:
                edited_count_values.append(i)
        requasted_k_count_values = []
        for req_k in range(k):
            requasted_k_count_values.append([req_k - 1])
            
        max_tekrar_nums = [num for num, tekrar in count.items() if tekrar == requasted_k_count_values]
        return (f"En çok tekrar eden sayı/sayılar: {max_tekrar_nums}, Tekrar sayısı: {requasted_k_count_values}")
        
            
        


so1 = Solution()
so1.topKFrequent([1,2,2,3,3,3],2)