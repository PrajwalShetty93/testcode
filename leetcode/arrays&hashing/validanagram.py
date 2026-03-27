class Solution:
    def isAnagram_Sorting(self, s: str, t: str) -> bool:
        # Check if length is different
        if len(s)!=len(t):
            return False
        
        s="".join(sorted(s))
        t="".join(sorted(t))

        if s==t:
            return True
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length is different
        if len(s)!=len(t):
            return False
        
        mapping_dict={}
        for i in s:
            if i in mapping_dict.keys():
                mapping_dict[i]=mapping_dict[i]+1
            else:
                mapping_dict[i]=1
        print(mapping_dict)

        for i in t:
            if i in mapping_dict.keys():
                mapping_dict[i]=mapping_dict[i]-1
            else:
                return False

        print(mapping_dict)
        for key, val in mapping_dict.items():
            if val>0:
                return False

        return True





sol=Solution()
s = "racecar"
t = "carrace"
print(sol.isAnagram_Sorting(s,t))
print(sol.isAnagram(s,t))




print('###################################    Learning    ##########################')

s="Python"
# Use sorted(str) to sort strings
print(sorted(s))
# To sort numbers use num.sort()

# Then use join to join arrays
print("".join(['a','b','c']))

print("".join(sorted(s)))

# To split words in a sentence
s="banana apple cherry"
print(sorted(s))
print(sorted(s.split()))