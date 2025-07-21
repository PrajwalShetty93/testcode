

from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.next=next
        self.val=val

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous= None

        while head:
            next_node=head.next
            head.next=previous
            previous=head
            head=next_node

        return previous
    
# 1 -> 2 -> 3 -> 4 -> None

# None -> 1 -> 2 -> 3 -> 4 -> None

# None <- 1   2 -> 3 -> 4 -> None

    # The trick here is to add an extra variable previous and set it to None
    # Now previous is None and head is 1
    # head.next to previous
    # Move the pointers, both head and previous
    # so previous =head
    # head = head.next, but since head.next is already assigned to previous, save it in a temp variable next_node
    # so, head = next_node





    def printList(self,head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
       
        
        
head = ListNode(1, ListNode(2, ListNode(3)))
sol=Solution()
sol.printList(head)

reverse = sol.reverseList_2(head)
sol.printList(reverse)

