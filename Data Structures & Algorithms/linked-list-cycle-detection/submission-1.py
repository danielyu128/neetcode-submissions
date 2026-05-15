# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = set()
        curr = head

        while curr:
            next_val = curr.next

            if next_val in vals:
                return True
            vals.add(next_val)
            curr = curr.next
        return False