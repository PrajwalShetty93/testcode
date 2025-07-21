# Input: s = "racecar", t = "carrace"

# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}
        for i in s:
            if i in anagram_dict:
                anagram_dict[i] = anagram_dict[i]+1
            else:
                anagram_dict[i]=1
        print(anagram_dict)


        for i in t:
            if i in anagram_dict:
                anagram_dict[i]=anagram_dict[i]-1
            else:
                return False
        print(anagram_dict)
        
        for k,v in anagram_dict.items():
            if v!=0:
                return False

        return True



sol =Solution()
s='racecar'
t='carrace'
print(sol.isAnagram(s,t))