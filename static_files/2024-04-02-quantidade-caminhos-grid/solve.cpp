matrix[0][0] = 1
for(i=1;i<n;i++)
    matrix[i][0] = 1;
for(j=1;j<n;j++)
    matrix[0][j] = 1;
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
    }
}