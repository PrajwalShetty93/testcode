from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map={}
        result=[]
        
        for i in nums:
            # if i in count_map:
            #     count_map[i]=count_map[i]+1
            # else:
            #     count_map[i]=1
            count_map[i]=count_map.get(i,0)+1
        print(count_map)

        # Sort the elements of the hashmap with values and return the top k elements
        # Time complexity O(n +n log n) = O(n log n)
        # Space Complexity O(n)
        count_map = sorted(count_map.items(),key = lambda x: x[1], reverse=True)
        print(count_map,)


        return [i[0] for i in count_map][:k]
    
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        
        count_map={}
        result=[]
        
        for i in nums:
           
            count_map[i]=count_map.get(i,0)+1
        print(count_map)

        bucket=[[]]* (len(nums)+1)                            #Never use this to create an empty list because it will create problems
        bucket1 = [[] for _ in range(len(nums) + 1)]
        print(bucket)
        print(bucket1)
        for k,v in count_map.items():
            bucket1[v].append(k)
        print(bucket1)

        for i in range(len(bucket1) - 1, 0, -1):
            print(bucket1[i])
            for num in bucket1[i]:
                print(num,bucket1[i])

        return []






            




sol=Solution()
nums = [1,2,2,3,3,3,3]
k = 2

result = sol.topKFrequent(nums,k)
print(result)

result = sol.topKFrequent_bucket(nums,k)
print(result)



print('TEST EXAMPLE~~~~~~~~~~~~~~~~~~~~~~')
test1 = [0]*5
test2 = [0 for _ in range(0,5)]
print(test1)
print(test2)

print('#########Sorting#############')
#Just by keys
freq_map = {1: 12, 2: 11, 3: 10}
sort_freq_map = sorted(freq_map)
print(sort_freq_map)

sort_freq_map = sorted(freq_map,reverse=True)
print(sort_freq_map)

#Sort by keys
sort_freq_map = sorted(freq_map.items())
print(sort_freq_map)

#Sort by values asc
sort_freq_map = sorted(freq_map.items(), key=lambda x: x[1])
print(sort_freq_map)

#Sort by values desc
sort_freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
print(sort_freq_map)

#Lambda example
square = lambda x: x*x
print(square(3))

add = lambda x,y: x+y
print(add(2,3))


sort_freq_map = sorted(freq_map.items(),key= lambda x:x[1])
print(sort_freq_map)
# Basically, the key looks at every example (3,10) and gets the x[1], which is 10 and then decides the logic