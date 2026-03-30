from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #Two pointer solution, keep l and r at extremes, and calculate area. area = distance * min height
        # move the smaller one inwards, because moving the larger one inwards wont increase area, but moving the smaller one might increase.
        

        # Time Complexity O(n) since at most one iteration.
        # Space complexity O(1) sinceno new data structures required


        l=0
        r = len(heights)-1

        maxArea = 0

        while (l<r):
            area = (r-l)* min(heights[l],heights[r])
            maxArea = max(area,maxArea)
            if heights[l] < heights[r]:
                l=l+1
            else:
                r=r-1
        return maxArea
        


sol=Solution()
height = [1,7,2,5,4,7,3,6]
height = [2,2,2]
res = sol.maxArea(height)
print(res)