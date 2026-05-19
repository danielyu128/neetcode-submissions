# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None:
            return head
        
        next_value = head.next
        next_value.next = head
        head.next = None
        self.reverseList(next_value)
