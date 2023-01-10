X = [[1,1,1],
    [1,1,1],
    [1,1,1]]
Y = [[1,1,1],
    [1,1,1],
    [1,1,1]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(Y)):
           result[i][j] =X[i][j] + Y[i][j]
for r in result:
    print(r)
