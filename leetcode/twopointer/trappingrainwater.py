from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        #My approach without 2 pointers
        #water in current  = min(max(l),max(r)) - height of current
        #So, compute 2 lists, max(l) and max(r)
        #very very important    , max(l) and max(r) should contain the current value as well

        # Time Complexity O(3n)=O(n) for iterating thrice
        # Space Complexity O(n)

        max_left_arr = [0 for _ in range(len(height))]
        max_right_arr = [0 for _ in range(len(height))]
        res = 0

        max_val = 0
        for i in range(0,len(height)):
            max_val = max(max_val,height[i])
            max_left_arr[i]=max_val

        max_val = 0
        for i in range(len(height)-1,-1,-1):
            max_val = max(max_val,height[i])
            max_right_arr[i]=max_val

        print(max_left_arr)
        print(max_right_arr)


        for i in range(len(max_right_arr)):
            res += min(max_left_arr[i],max_right_arr[i])-height[i]


        return res

    def trap_2pointer(self, height: List[int]) -> int:

        # This is tricky and honestly took me some time to understand.
        # Previous ex:
        # [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]

        # keep l and r at extremes. Calculate max_l and max_r on the go.
        # The logic is that if max_l <= max_r, water is dependent on min_val, which is max_l, so use that in cal and move left +1

        # If max_r < max_l, that means water is dependent on max_r and move r inwards. 


        l=0
        r=len(height)-1
        max_l = 0
        max_r = 0
        res = 0
        res_l=[]


        while (l<r):
            max_l = max(height[l],max_l)
            max_r = max(height[r],max_r)

            if max_l <=max_r:
                res += (max_l - height[l])
                res_l.append(max_l - height[l])

                l+=1
            else:
                res += (max_r - height[r])
                res_l.append(max_r - height[r])
                r -=1
        print(res_l)
        return res



height = [0,2,0,3,1,0,1,3,2,1]
sol =Solution()
res = sol.trap(height)
print(res)

res = sol.trap_2pointer(height)
print(res)
