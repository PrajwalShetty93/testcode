

matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target=34
target_matrix=[]
for m in matrix:

    if target<= m[-1]:
        target_matrix=m
        break;

print(target_matrix)

