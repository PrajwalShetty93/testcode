from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)
        # rows = {}
        # cols = {}
        # boxs= {}    This doesnt work. see below
        
        print(rows)
        for row in range(len(board)):
            for col in range(len(board[row])):
                
                box_index=(row//3,col//3)

                val = board[row][col]
                if val=='.':
                    continue

                # print(board[row][col])
                if val in rows[row] or val in cols[col] or val in boxs[box_index]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxs[box_index].add(val)


        return True   







board =[["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

sol=Solution()
res = sol.isValidSudoku(board)
print(res)

print('############Test##############')
print(10/3)
print(10//3)
print(10%3)

dict = collections.defaultdict(set)
print(dict)


dict = collections.defaultdict()
print(dict)

dict = collections.defaultdict(list)
print(dict)




dict = {}
dict[24]=[47]
print(dict)
dict[24].append(48)
print(dict)
# works because you first initialised it with 47. If it was empty.

dict={}
# dict[24].append(48)
print(dict)  #This fails because list is empty.

dict =collections.defaultdict(list)
dict[24].append(48)
print(dict)

dict = collections.defaultdict(int)
dict[24]=dict.get(24,0)+1
print(dict)