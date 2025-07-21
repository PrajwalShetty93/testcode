from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        

        for i in range(len(cost)-3,-1,-1):
            cost[i]=min(cost[i]+cost[i+1], cost[i]+cost[i+2])

        return min(cost[0],cost[1])



cost = [1,2,3]
sol=Solution()
res = sol.minCostClimbingStairs(cost)
print(res)

print('*'*20)
nums=[1,2,3,4,5]
for i in range(0,len(nums)):
    print(nums[i])
print('*'*20)
for i in range(len(nums)-3, -1, -1):
    print(nums[i])   