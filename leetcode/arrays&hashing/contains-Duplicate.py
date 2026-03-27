


from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output=set()
        for i in nums:
            if i in output:
                return True
            output.add(i)
        return False

# Time complexity O(n)
# Space Coplexity O(n)



sol= Solution()
nums = [1, 2, 3, 4]
print(sol.hasDuplicate(nums))


# Now to convert list into set,, you can use set(nums)
# Then you can use len(nums) != len(set(nums))


# Trick question, can you do the space complexity in O(1).
# which means not creating a new list/set.
# The solution is to sort the elements and compare the previous element to the next element,(but time complexity is O nlogn becuse of sort)
# This will need java style loops, int i=0;i<...
# In python, its done by range(1,len(nums)), then nums[], or range(0,len(nums))

def contains_Duplicate_sort(nums):
    nums.sort()

    for i in range(1,len(nums)):


        if nums[i] == nums[i-1]:
            return True
        
    return False


# Remember nums.sort() for numbers, space complexity O(1) because not saved in new memory
# and abc="".join(sorted(abc)) for strings, Space complexity O(n) because it returns a new list