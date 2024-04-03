n = 5
m = 5
matrix = [ [0 for _ in range (m)] for _ in range(n)]
matrix[0][0] = 1
for i in range(1,n):
    matrix[i][0] = 1
for j in range(1,m):
    matrix[0][j] = 1

for i in range(1,n):
    for j in range(1,m):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for row in matrix:
    for x in row:
        print(x,end=' ')
    print('')