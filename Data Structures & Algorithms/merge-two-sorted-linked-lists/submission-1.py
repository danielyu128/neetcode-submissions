# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_list1, curr_list2 = list1, list2
        dummy = None
        if curr_list1 is not None and curr_list2 is not None:
            if curr_list1.val <= curr_list2.val:
                dummy = curr_list1
                curr_list1 = curr_list1.next
            else:
                dummy = curr_list2
                curr_list2 = curr_list2.next

        elif curr_list1 is None and curr_list2 is None:
            return curr_list1
        
        elif curr_list2 is None:
            return curr_list1
        else:
            return curr_list2

        while curr_list1 or curr_list2:
            
            if curr_list1.val <= curr_list2.val:
                next_val = curr_list1.val
                dummy.next = next_val
                curr_list1 = curr_list1.next
            else:
                next_val = curr_list2.val
                dummy.next = next_val
                curr_list2 = curr_list2.next

        return dummy
            