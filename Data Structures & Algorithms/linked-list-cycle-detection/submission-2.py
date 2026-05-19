# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head

        while curr and curr.next:
            if curr == curr.next:
                return True
            curr = curr.next
            curr.next = curr.next.next

        return False