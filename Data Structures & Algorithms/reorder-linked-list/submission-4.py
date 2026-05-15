# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# I have to figure out how to split the linked list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None

        while second_half:
            next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next

        second_half = prev
        start = head

        while second_half:
            temp1, temp2 = start.next, second_half.next
            start.next = second_half
            second_half.next = temp1
            start, second_half = temp1, temp2



