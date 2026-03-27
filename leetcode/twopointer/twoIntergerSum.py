from typing import List

# Time Complexity 0(n)
# Space COmplexity O(1) since two variables were created, no new data Structure used
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r:
            print(numbers[l],numbers[r])
            if numbers[l]+numbers[r]==target:
                return [numbers[l],numbers[r]]
            if numbers[l]+numbers[r]< target:
                l=l+1
            if numbers[l]+numbers[r]> target:
                r=r-1
        
        return []


numbers = [1,2,3,4]
target = 6
sol=Solution()
print(sol.twoSum(numbers,target))


# Twosum can be solved both by 2 pointers as well as Array and Hashmap solution