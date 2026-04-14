import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach:
        # window smallest l and r set to 0
        # calculate freq hashmap
        # increase r and recompuet hashmap freq.
        # initially thought of using smallest value from freq map, but realised this will work only when there are 2 characters in the input. 
        # So, window length  - max freq, gives the different letter.
        # window_length-max <k, increment r
        # else move l to +1    

        # s = "XYYXABC"

        l=0
        r=0
        freq_map = collections.defaultdict(int)
        res= 0

        print(freq_map)

        while l<=r and r<(len(s)):
            freq_map[s[r]]=freq_map.get(s[r],0)+1
            max_freq = max(freq_map.values())
            window_size = r-l+1
            if window_size - max_freq <= k:
                res = max(res,window_size)
                r=r+1
                
            else:
                while (window_size - max_freq) > k:
                    freq_map[s[l]]= freq_map.get(s[l]) - 1
                    max_freq = max(freq_map.values())
                    window_size = r-l+1
                    if freq_map[s[l]]==0:
                        del freq_map[s[l]]
                    l=l+1
                

        return res
    


    def characterReplacement_forLoop(self, s: str, k: int) -> int:
        res=0
        l=0
        freq_map = collections.defaultdict(int)
        for r in range(len(s)):
            freq_map[s[r]]=freq_map.get(s[r],0)+1
            max_freq = max(freq_map.values())
            window_size = r-l+1
            if window_size - max_freq <=k:
                res= max(res,window_size)
            else:
                while window_size - max_freq > k:
                    freq_map[s[l]]=freq_map[s[l]]-1
                    if freq_map[s[l]]==0:
                        del freq_map[s[l]]
                    l=l+1
                    window_size =  r-l+1
                    max_freq = max(freq_map.values())
        return res

sol = Solution()
s = "XYYXABC"
s= "AABABBA"
k = 1
# res = sol.characterReplacement(s,k)
res = sol.characterReplacement_forLoop(s,k)
print(res)