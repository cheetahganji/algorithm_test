def solution(m, n, puddles):
    answer = 0
    
    grid = [ [-1 for x in range(m)] for y in range(n) ]
    grid[0][0] = 1

    if puddles:
        for i in puddles:
            grid[i[1]-1][i[0]-1] = 0

    for i in range(1, m):
        if grid[0][i] == -1:
            grid[0][i] = grid[0][i-1]

    for i in range(1, n):
        if grid[i][0] == -1:
            grid[i][0] = grid[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == -1:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    answer = grid[n-1][m-1] % 1000000007

    return answer
