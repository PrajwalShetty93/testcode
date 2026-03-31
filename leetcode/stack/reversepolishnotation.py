
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        input_stack = []

        for token in tokens:
            try:
                digit = int(token)
                input_stack.append(digit)
            except Exception as e:
                b = input_stack.pop()
                a = input_stack.pop()
                input_stack.append(self.calculate(a,b,token))
        return input_stack.pop()
            

    def calculate(self,a,b,operator):
        if "+" in operator:
            return a+b
        elif "-" in operator:
            return a-b
        elif "*" in operator:
            return a*b
        elif "/" in operator:
            return int(a/b)








tokens = ["1","2","+","3","*","4","-"]
sol = Solution()
res = sol.evalRPN(tokens)
print(res)