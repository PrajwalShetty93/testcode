from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
    # Can be solved by 2 pointers as well as hashmap difference solution.
    # With 2 pointer solution, Space Complexity is 0(1), with hashmap its 0(n)


    # TIme complexity is O(n2) because of 3,2,1 iterations, (n-1) + (n-2) + ... + 1 = n*(n-1)/2 ≈ O(n²)
    # Space complexity is O(1) because een though its an array returned, it can be constant, 
    # it cant be array of n size, it is of 2 size because 2 elements in the output always , so O(2)=O(1)
    def twoSum_BruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                print("i:"+str(nums[i])+" j:"+str(nums[j]))
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


nums = [3,4,5,6]
target = 7
sol=Solution()
print(sol.twoSum_BruteForce(nums,target))


# Prints only 0,1,2,3  doesnt print 4
for i in range(0,4):
    print(i)