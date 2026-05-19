# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# I have to figure out how to split the linked list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
# [2,4] [10,8,6]

# 2,10,4,8,6

# [2,4] [8,6]

# 2,8,4,6
        length = 0
        while curr:
            curr = curr.next
            length+=1

        start_size = length // 2

        count = 0

        start = head
        end = ListNode()

        while count < start_size:
            start = start.next
            count+=1
            if count == start_size:
                end = start
                start.next = None

        prev = None
        end_pointer = end

        while end_pointer:
            next_val = end_pointer.next
            end_pointer.next = prev
            prev = end_pointer
            end_pointer = next_val

        end_node = prev


        #this next part I have to alternatively merge the list together
        #Head node is called start, tail node is called end_node

        #I think i will need a dummy, a head, and a boolean that 
        # tracks which one you need to input into the linked list

        dummy = ListNode()
        current = dummy
        alternating = True
        while start and end_node:
            print("In loop")
            if alternating:
                current.next = start
                start = start.next
                alternating = False
                print(f"Number {current.val}")
            else:
                current.next = end_node
                end_node = end_node.next
                alternating = True
                print(f"Number {current.val}")
            current = current.next

        if start:
            current.next = start
        elif end_node:
            current.next = end_node

        return dummy.next




