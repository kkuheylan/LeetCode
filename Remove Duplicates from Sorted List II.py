# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sorted_head = []
        # for sorting_num in head:
        #     if sorting_num not in sorted_head:
        #         if sorted_head == []:
        #             sorted_head.append(sorting_num)
        #         else:
        #             if sorting_num < sorted_head[0]:
        #                 sorted_head.insert(0,sorting_num)
        #             else:
        #                 for swap in sorted_head:
        count=0
        def len_link(list):
            temp=list.head
            while(temp):
                count+=1
                temp=temp.next
        
        for i in range(count - 1):
            if head[i] > head[i+1]:
                pos1 = head.index(i)
                pos2 = head.index(i+1)
                head[pos1], head[pos2] = head[pos2], head[pos1]     

        for i in head:
            if head.count(i) != 1:
                del_index = head.index(i)
                head = head.pop([del_index])
        return head
    
# not finished yet!
    
    
    
    
    
    
