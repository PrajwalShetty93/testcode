from typing import List


class Solution:
    # Time complexity O(n2) 
    # sort O(nlogn) timsort
    # for loop O(n)
    # while loop o(n)
    # Final list conversion O(k)

    # Space complexity resultset (O(n+k)) where k is the number of triplets and n is for sort
    # Optimum solution is not to use a set. compare the element with the previous one
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()

        for i in range(0,len(nums)):

            l=i+1
            r=len(nums)-1
            while(l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    result.add((nums[i],nums[l],nums[r]))
                    l=l+1
                elif nums[i]+nums[l]+nums[r] >0:
                    r=r-1                               # I had this reverse, hence it failed, see explanation 
                elif nums[i]+nums[l]+nums[r] <0:
                    l=l+1

        return [list(res) for res in result]
    
    #Got confused: 1,2,3,4,7
    # target =6
    # l=1, r=7 total=8
    # total>target, so move r backwards
    # if total <target, move l forwards

# Without the set
    def threeSum_Optimum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]

        for i in range(0,len(nums)):

            l=i+1
            r=len(nums)-1

            # This basically checks if the element is same as previous, if its same that means it 
            # already has been tested before and can be skipped, eliminating the need for a set.
            if i > 0 and nums[i]==nums[i-1]:
                continue
            while(l<r):
                
                if nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while l < r and nums[l] == nums[l-1]:  # ✅ skip duplicate l, this is for solution [0,0,0,0], see below
                        l += 1
                elif nums[i]+nums[l]+nums[r] >0:
                    r=r-1                               # I had this reverse, hence it failed, see explanation 
                elif nums[i]+nums[l]+nums[r] <0:
                    l=l+1

        return result
    
# What's Happening
# With nums = [0, 0, 0, 0] after sorting → [0, 0, 0, 0]
# i=0, l=1, r=3, sum=0  → ✅ append [0,0,0], l → 2
# i=0, l=2, r=3, sum=0  → ✅ append [0,0,0] again ❌ (duplicate!)
# i=1, l=2, r=3         → ⏭️  skipped (nums[1] == nums[0])
# i=2, l=3, r=3         → ⏭️  skipped (nums[2] == nums[1])

    def threeSum_BruteForce(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        resultset=set()

        # O(n4) time complexity
        # Space complexity O(n+k) where k is the number of triplets and n is for sort
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        if not [nums[i],nums[j],nums[k]] in result:  #This was added to avoid duplicates, but the problem is this will iterate t
                            # the result list again and increase the time complexity to O(n4). Instead use a set
                            result.append([nums[i],nums[j],nums[k]])

        # O(n3) time complexity
        # Space complexity O(n+k) where k is the number of triplets and n is for sort
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                            resultset.add((nums[i],nums[j],nums[k]))

            
        return [list(result) for result in resultset]

        


sol=Solution()
nums = [-1,0,1,2,-1,-4]
output = sol.threeSum_BruteForce(nums)
output2 = sol.threeSum(nums)
output3 = sol.threeSum_Optimum(nums)
print(output)
print(output2)
print(output3)


##########Learning
# You can use 
# for i in range(0,len(nums)):
#     print(i,nums[i])

# or 
# for i,a in enumerate(nums):
#     print(i,a)


# set to list conversion
test1= (1,2,3,4,5)
test2=list(test1)
print(test2)

test1 = ((1,2,3),(2,3,4),(3,4,5))
test2=list(test1)
print(test2)
# this returns [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
test2 = [list(t) for t in test1]
print(test2)