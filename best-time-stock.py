'''Input: prices = [10,4,5,6,2,1,8]

Output: 6
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1

        max_profit=0
        while(r<len(prices)):
            if (prices[r]>prices[l]):
                max_profit=max(prices[r]-prices[l],max_profit)
                r+=1
            else:
                l=r
                r+=1
        return max_profit


        



sol=Solution()
prices=[7,1,5,3,6,4]

print(sol.maxProfit(prices))