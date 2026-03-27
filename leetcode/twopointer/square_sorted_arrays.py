'''
Input: `[-3, -2, -1, 0, 4, 5]`
Output: `[0, 1, 4, 9, 16, 25]`
'''


class Solution:
    def sortedSquares(self,nums):
        l=0
        r=len(nums)-1
        output = [None] * len(nums)
        last_digit=len(nums)-1

        while(l<=r):

            if nums[l]*nums[l] < nums[r]*nums[r]:
                output[last_digit]=nums[r]*nums[r]
                r=r-1
            else:
                output[last_digit]=nums[l]*nums[l]
                l=l+1
            last_digit-=1
        return output





sol=Solution()
input=[-3, -2, -1, 0, 4, 5]
input=[1,2,3,4,5,6]

print(sol.sortedSquares(input))

