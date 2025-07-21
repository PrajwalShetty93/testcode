# list1 = [1,2,4], list2 = [1,3,5]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output=ListNode()
        current=output

        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            printList(output)
            current=current.next
            
        current.next = list1 if list1 else list2
        
        
        return output.next
    
def printList(head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    

sol=Solution()
list1=ListNode(1)
list1.next=ListNode(3)
list1.next.next=ListNode(5)

list2=ListNode(2)
list2.next=ListNode(4)
list2.next.next=ListNode(6)
printList(list1)
printList(list2)
list3 = sol.mergeTwoLists(list1,list2)

printList(list3)


# Again very basic but I made lots of mistakes
# 1 -> 3 -> 5   ,  2 -> 4 -> 6

# Create a new ListNode(). This will be head which we will return
# Create a current variable, which will be moving
# Compare between list1 and list2 val,
# current.next will be l1 or list2move current to nextat the end, add all extra values.
# return the output.next as the first value was dummy
# See the printlist(output) to see how it performs