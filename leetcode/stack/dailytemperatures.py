from typing import List

class Solution:
    # I was wondering how to keep the order of the index with the value. seems like I was thinking too much.
    #  Initially thought of using a hashmap, put a list of pair is fine as well. See below stack
    # Each element is:
    # → pushed onto stack ONCE
    # → popped from stack ONCE, so time is O(2n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]


        for i , temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
            else:
                while stack and temp > stack[-1][1]:
                    temp_pair = stack.pop()
                    res[temp_pair[0]] = i-temp_pair[0]
                
                stack.append((i,temp))


        return res



sol=Solution()

temperatures = [30,38,30,36,35,40,28]
# temperatures = [22,21,20]
res = sol.dailyTemperatures(temperatures)
print(res)