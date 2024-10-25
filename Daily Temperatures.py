# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         for left in range(len(temperatures)):
#             found_high = False
#             for right in range(left + 1, len(temperatures)):
#                 if temperatures[left] < temperatures[right]:
#                     index_gap = right - left
#                     result.append(index_gap)
#                     found_high = True
#                     break
#             if not found_high:
#                 result.append(0)
#         return result

#link: https://leetcode.com/problems/daily-temperatures/