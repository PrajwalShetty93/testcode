nums = [-1,0,2,4,6,8]
target=4
# output=3


from typing import List


class Solution:
    def search_bruteforce(self, nums: List[int], target: int) -> int:
        index=0
        for i in nums:
            if i == target:
                return index
            index=index+1


    def search_binary(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        count=0

        while(l<=r):
            mid=int((r+l)/2)  # I made a mistake of calculating the mid, it should be l+r/2 not r-l/2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                l=mid+1   # Add this to have the window shrink, else infinite loop
            else:
                r=mid-1  # Same
            count=count+1
            if count >5:
                break        

        return -1


        
sol=Solution()
print(sol.search_bruteforce(nums,target))
print(sol.search_binary(nums,target))



nums = [-1,0,2,4,6,8]
target=4

            