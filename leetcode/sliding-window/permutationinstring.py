import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

#     compute freq map of s1:
#     window size of s1
#     first compute windowsize, keep moving window +1, modify the freq_map and check, if match return True
# else return false, until r is at the end
# Use for r in as its easier to understand

        if len(s1)>len(s2):
            return False
        
        l=0
        r=len(s1)
        s1_map = collections.defaultdict(int)
        s2_map = collections.defaultdict(int)
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i],0)+1

        for i in range(len(s1)):
            s2_map[s2[i]] = s2_map.get(s2[i],0)+1
        
        if s1_map == s2_map:
            return True
        


        for r in range( len(s1) , len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r],0)+1
            s2_map[s2[l]] = s2_map.get(s2[l],0)-1
            if s2_map[s2[l]] ==0:
                del s2_map[s2[l]]
            l=l+1
            if s1_map == s2_map:
                return True
        
        return False


sol=Solution()
s1 = "abc"
s2 = "lecabee"
res = sol.checkInclusion(s1,s2)
print(res)

