def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    n = len(arr)
    
    for i in range(n):
        primary_diagonal_sum += arr[i][i]           # Primary diagonal: arr[0][0], arr[1][1], ...
        secondary_diagonal_sum += arr[i][n - i - 1] # Secondary diagonal: arr[0][n-1], arr[1][n-2], ...
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


n = int(input().strip())  

arr = []  

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))


result = diagonalDifference(arr)

print(result)
