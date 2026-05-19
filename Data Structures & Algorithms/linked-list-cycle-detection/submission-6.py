# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        next = head.next.next
        while curr or next:
            if curr == next:
                return True
            curr = curr.next
            next = curr.next.next

        return False