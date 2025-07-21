# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        index = 0

        for i in nums:

            if (target-i) in num_map:
                return sorted([index, num_map[target-i]])
            else:
                num_map[i]=index
            index+=1  
        
        return []
    
nums=[3,4,5,6]
target=9
sol=Solution()
result = sol.twoSum(nums,target)
print(result)
