'''Input: prices = [10,4,5,6,2,1,8]

Output: 6
'''
from typing import List
class Solution:
    # TIme complexity O(n) since 1 while Loop
    # Space Complexity O(1)
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        profit=0

        while(l<r and r <len(prices)):
            if prices[r]-prices[l]>0:
                profit=max(prices[r]-prices[l],profit)
                r=r+1
            else:
                l=r
                r=r+1

        return profit

        



sol=Solution()
prices=[7,1,5,3,6,4]

print(sol.maxProfit(prices))