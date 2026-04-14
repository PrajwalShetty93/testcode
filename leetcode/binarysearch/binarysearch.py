from typing import List

# (r+l)/2

# Mistakes which I made:
# while (l<=r), before I had (l<r), this meant, when both l&r was at 3, it skipped instead of checking
# r=m-1 and l=l+1, I didnt add +1, because of which it stayed the same on every loop
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r= len(nums)-1

        while (l<=r):
            m = (r+l)//2
            if nums[m] == target:
                return m
            elif nums[m] >target:
                r= m-1
            elif nums[m] <target:
                l=m+1
        return -1 




nums = [-1,0,2,4,6,8]
target = 4
sol=Solution()
res = sol.search(nums,target)
print(res)

