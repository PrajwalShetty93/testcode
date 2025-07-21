# Input: s = "Was it a car or a cat I saw?"

# Output: true

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<=r:
            print('l:',s[l])
            print('r:',s[r])
            if  not bool(re.match(r'^[a-zA-Z0-9]$', s[l])):
                l=l+1
            if  not bool(re.match(r'^[a-zA-Z0-9]$', s[r])):
                r=r-1

            if s[l].lower() == s[r].lower():
                l=l+1
                r=r-1
            else:
                return False
        
        return True
    
sol=Solution()
s="Was it a car or a cat I saw?"
print(sol.isPalindrome(s))