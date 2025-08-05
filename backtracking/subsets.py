from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        
        def dfs(i):
            print(str(i)+' : '+str(subset))
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        
        
        dfs(0)
        return res
        






sol  = Solution()
nums = [1,2,3]
res = sol.subsets(nums)
print(res)