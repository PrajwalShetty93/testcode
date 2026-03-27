import re

class Solution:

    # TIme complexity is 0(n) because every letter is only checked once, only 1 iteration or loop.
    # Space Complexity, only 2 variables, l&r, even if the size of input is 500 characters, we'll still be using only 2 variables
    # hence constant space 0(1)
    def isPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1

        while l<=r:

            if not s[l].isalnum():
                l=l+1
                continue
            if not s[r].isalnum():
                r=r-1
                continue   
            # Added continue because if ???? exists continue will make sure, if skips everything, without continue it will just skip the first occurence

            if str(s[l]).lower().__eq__(str(s[r]).lower()):
                l=l+1
                r=r-1
            else:
                return False


        return True



s = "Was it a car or a cat I saw??"
sol =Solution()
print(sol.isPalindrome(s))