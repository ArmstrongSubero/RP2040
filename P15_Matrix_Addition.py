A = [[5, 4, 2],
     [6, 3, 1],
     [2, 8, 3]]

B = [[2, 4, 2],
     [0, 4, 10],
     [8, 2, 8]]

res = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

# Matrix addition
for i in range(len(A)):
    for j in range(len(A[0])):
        res[i][j] = A[i][j] + B[i][j]

# Print the result
for i in res:
    print(i)
