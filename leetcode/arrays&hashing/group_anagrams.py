from typing import List


# Time complexity O(n x klogk) where n is the for loop and k logk is for the sorted
# Space Complexity O(n x k) where n is the number of words and k is the max length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = {}
        for i in strs:
            sorted_str = "".join(sorted(i))      #Earlier I had sorted(i) and it returned ['a', 'c', 't']
            
            if sorted_str in sorted_dict.keys():
                sorted_dict[sorted_str].append(i)
            else:
                sorted_dict[sorted_str]=[i]

        print(sorted_dict)
        result = [values for values in sorted_dict.values()]
        # could also be result = list(sorted_dict.values)

        return result
        





sol= Solution()
strs = ["act","pots","tops","cat","stop","hat"]
result = sol.groupAnagrams(strs)
print(result)