class Solution:

    # for sliding window, try to use for r in range(len), because window ends at the last element, unlike 2 pointers
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        r=0
        resultSet = []
        maxLength=0

        while (l<=r and r < len(s)):
            if not s[r] in resultSet:
                resultSet.append(s[r])
                maxLength=max(maxLength,len(resultSet))
                r=r+1
            else:
                while resultSet:
                    out = resultSet.pop(0)
                    l=l+1
                    if str(out).__eq__(s[r]):
                        break
        return maxLength

# 2 errors: This is a O(n2) solution only because I used a list for tracking. If I had used a set, it would be O(n)
#  I used list because I couldnt figure out how to remove elements from the set in order
# Operation  List   Set 
# in check  O(n)    O(1)   #Main culprit for O(n)
# add       O(1)    O(1)
# remove    O(n)    O(1)

    def lengthOfLongestSubstring_Optimum(self, s: str) -> int:

        l=0
        r=0
        resultSet = set()
        maxLength=0

        while (l<=r and r < len(s)):
            if not s[r] in resultSet:
                resultSet.add(s[r])
                maxLength=max(maxLength,len(resultSet))
                r=r+1
            else:
                while s[r] in resultSet:
                    resultSet.remove(s[l])
                    l=l+1

        return maxLength



sol=Solution()
s = "zxyzxyzbde"
output = sol.lengthOfLongestSubstring(s)
print(output)
output2 = sol.lengthOfLongestSubstring_Optimum(s)
print(output2)
