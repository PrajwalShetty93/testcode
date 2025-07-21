'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
'''


'''Use a set or a hashmap contains'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers=set() '''set declaration'''
        for num in nums:
            if num in numbers:
                return True
            numbers.add(num)
        return False


