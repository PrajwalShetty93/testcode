
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_list = nums
        heapq.heapify(self.heap_list)

        while len(self.heap_list) > k:
            heapq.heappop(self.heap_list)


    def add(self, val: int) -> int:
        if len(self.heap_list)< self.k:
            heapq.heappush(self.heap_list,val)
        else:    
            heapq.heappushpop(self.heap_list,val)
        return self.heap_list[0]


kthLargest = KthLargest(3, [1, 2, 3, 3]);

print(kthLargest.add(3))
# // return 3
print(kthLargest.add(5));
# // return 3
print(kthLargest.add(6));
# // return 3
print(kthLargest.add(7));
# // return 5
print(kthLargest.add(8));
# // return 6

