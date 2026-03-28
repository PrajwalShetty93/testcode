from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res = res + str(len(word))+"#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res= []
        while(i<len(s)):
            # val = int(s[i])
            val = int(s[i:s.index('#',i)])
            beginIndex = s.index('#',i)+1

            endIndex = beginIndex+val
            word = s[beginIndex : endIndex]
            res.append(word)
            i=val+beginIndex

        return res
    
    def decode_1(self, s: str) -> List[str]:

        res = []

        while s:
            value = int(s[:s.index('#')]) 
            beginIndex = s.index('#')+1
            endIndex = beginIndex+value
            word = s[beginIndex:endIndex]
            res.append(word)
            s=s[endIndex:]


        return res



sol= Solution()
dummy_input = ["Hello","World"]

dummy_input=["we","say",":","yes","!@#$%^&*()"]
encoded_val = sol.encode(dummy_input)
print(encoded_val)
decoded_val = sol.decode_1(encoded_val)
print(decoded_val)