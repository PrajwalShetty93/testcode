from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow:
                return True

        return False




nodes = [ListNode(i) for i in range(4)]
for i in range(3):
    nodes[i].next = nodes[i+1]
# nodes[4].next = nodes[2]

head = nodes[0]

sol=Solution()
result = sol.hasCycle(head)
print(result)

# Couple of mistakes here., start both slow and fast at head
# check if fast and fast.next is not empty

# Learnt something new
# Lets say 1 -> 2 -> 3
# fast is pointing to 1, fast.next=2, fast.next.next=3
# Now fast.next is None, so all good, loop ends

# Lets say 1 -> 2 -> 3 -> 4
# fast is pointing to 1, fast.next=2, fast.next.next=3
# Now fast.next is 4, fast.next.next=None, which is still fine. Hence we check fast and fast.next is not None
# You cant use the values of None though but no NoneError



