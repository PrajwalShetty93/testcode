import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:   
        # heapq._heapify_max(stones)    
        # This doesnt work properly, because heapify_max builds max_heap but heap.pop pops out min value.
        
        stones = [-i for i in stones]
        heapq.heapify(stones) 

        while len(stones)>1:
            max1= heapq.heappop(stones)
            max2= heapq.heappop(stones)
            if max2-max1>0:
                heapq.heappush(stones,-(max2-max1))
        
        if len(stones)==1:
            return abs(stones[0])
        else:
            return 0




sol =Solution()
stones = [2,3,6,2,4]
result = sol.lastStoneWeight(stones)
print(result)
