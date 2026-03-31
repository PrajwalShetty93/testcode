import collections
class Solution:

# """
# I tried with the following approach. The approach is correct, might take some time but still correct. However theres a bug, 
# Every after the run, the last window is valid, but the while loop exists and hence the last window is never executed. Fixed after adding break statement so that s[r] is not calculated 
# """

# A better solution would be to use a for loop for r keep increasing the size of r and if conditions are met, shrink the l in the while loop



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
        # res_list = []


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
                
                # res_list.append(s[l:r])
                s_map[s[l]]=s_map.get(s[l],0)-1
                l=l+1
                
        # print(res_list)
        return res


    def minWindow_forLoop(self, s: str, t: str) -> str:

        if (len(t)>len(s)):
            return ""
        
        t_map = collections.defaultdict(int)
        s_map = collections.defaultdict(int)
        res_list = []

        for i in range(len(t)):
            t_map[t[i]]=t_map.get(t[i],0)+1
        
        l=0
        for r in range(0, len(s)):
            s_map[s[r]]=s_map.get(s[r],0)+1
            substring_exists=True
            for k,v in t_map.items():
                if not (k in s_map and v<=s_map[k]):
                    substring_exists=False
                    break

            while substring_exists:
                res_list.append(s[l:r+1])
                s_map[s[l]]=s_map.get(s[l],0)-1
                l=l+1
                substring_exists=True
                for k,v in t_map.items():
                    if not (k in s_map and v<=s_map[k]):
                        substring_exists=False

        return res_list




sol=Solution()
s = "OUZODYXAZV"
t = "XYZ"
s = "ADOBECODEBANC"
t="ABC"

# result = sol.minWindow(s,t)

res = sol.minWindow_forLoop(s,t)
print(res)
        

