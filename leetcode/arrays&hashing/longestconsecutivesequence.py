from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_len = 0
        for num in nums:
            length=0
            if num-1 in nums:
                continue
            else:
                curr = num
                while curr in nums:
                    length=length+1
                    curr= curr+1
                    max_len=max(length,max_len)
                    

        return max_len
        

# #Why is it NOT O(n²)?
# The while loop only runs when a number is a sequence start. Every number is visited at most twice across the entire algorithm:

# Space COmplexity O(n)


nums = [2,20,4,10,3,4,5]
sol=Solution()
res = sol.longestConsecutive(nums)
print(res)