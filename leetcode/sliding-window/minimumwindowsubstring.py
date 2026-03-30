import collections
class Solution:

# """
# I tried with the following approach. The approach is correct, might take some time but still correct. However theres a bug, 
# Every after the run, the last window is valid, but the while loop exists and hence the last window is never executed. 
# """


    def minWindow(self, s: str, t: str) -> str:
        
        if (len(t)>len(s)):
            return ""
        
        t_map = collections.defaultdict(int)
        s_map = collections.defaultdict(int)
        
        for i in range(len(t)):
            t_map[t[i]]=t_map.get(t[i],0)+1
        
        l=0
        r=0
        res=""
        res_list = []
        "ABCDE"

        while(l<=r) and r<=len(s):
            substring_exists = True
            for k,v in t_map.items():
                if not (k in s_map and v <= s_map[k]):
                    substring_exists=False
                    break
            
            if not substring_exists:
                if r < len(s):
                    s_map[s[r]]=s_map.get(s[r],0)+1
                    r+=1
                else:
                    break
               

            else:
                if not res:
                    res = s[l:r]
                else:
                    if len(s[l:r]) <len(res):
                        res = s[l:r]
                
                res_list.append(s[l:r])
                s_map[s[l]]=s_map.get(s[l],0)-1
                l=l+1
                
        print(res_list)
        return res





sol=Solution()
s = "OUZODYXAZV"
t = "XYZ"
s = "ADOBECODEBANC"
t="ABC"

result = sol.minWindow(s,t)
print(result)
        

