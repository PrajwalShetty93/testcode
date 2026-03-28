from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        1,2,4,6
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]
        product= 1
        for i in range(len(nums)):
            if i != 0:
                product=product * nums[i-1]
                prefix[i]=product


        product = 1
        for i in range(len(nums)-1,-1,-1):
            if i != len(nums)-1:
                product=product * nums[i+1]
                postfix[i]=product
            
        
        for i in range(len(postfix)):
            postfix[i]=postfix[i]*prefix[i]

        return postfix




sol= Solution()
nums = [1,2,4,6]
# nums = [2,3,4,6]
res = sol.productExceptSelf(nums)
print(res)


for i in range(0,5):
    print(i)

for i in range(5,0,-1):   #It will skip 0, so for list iteration in reverse,use -1 to stop  range(start,stop,step)
    print(i)

