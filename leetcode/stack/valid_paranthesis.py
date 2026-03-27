class Solution:

    # TimeO(n) — single pass through string
    # SpaceO(n) — stack worst case holds all characters
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        stack = []
        for char in s:
            if char in bracket_map:
                
                last_element = (stack.pop()) if stack else ""
                if not bracket_map[char].__eq__(last_element):
                    return False
                    

            else:
                stack.append(char)
        
        if len(stack)==0:
            return True
        return False




sol= Solution()
s = "([{}]))"
output = sol.isValid(s)
print(output)


# To get the last element, i.e peek, use stack[-1]