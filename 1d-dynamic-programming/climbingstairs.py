


class Solution:
    def climbStairs(self, n: int) -> int:
        # two variables
        one=1
        two=1


        # navigate from 0 to 4
        for i in range (0,n-1):
        
            total = one+two
            two=one
            one=total
        return one




sol=Solution()
n=3
res = sol.climbStairs(n)
print(res)

