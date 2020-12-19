"""
    GOLD MINING PROBLEM

    PROBLEM DESCRIPTION

        Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount 
        of gold in tons. Initially the miner is at first column but can be at any row. He can move only
        (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up
        towards the right or right or diagonally down towards the right. Find out maximum amount of gold 
        he can collect.

        Eg, 
            Input : mat[][] =  {{1, 3, 3},
                                {2, 1, 4},
                                {0, 6, 4}};
            Output : 12 
            {(1,0)->(2,1)->(2,2)}

    SOLUTION
        For a every column, take the maximum of left, left-up, left-down elements and add it with the column value to get
        the max value for the column. 

        DP[i][j] = AR[i][j] + MAX( DP[i][j-1], DP[i-1][j-1], DP[i+1][j-1] ) 

"""

def gold_mining(ar, m, n):
    dp = [ [0 for i in range(n)] for i in range(m) ]

    for j in range(n):
        for i in range(m):
            if j == 0:
                dp[i][j] = ar[i][j]
            elif i == 0 and j > 0:
                v = max(dp[i][j-1], dp[i+1][j-1])
                dp[i][j] = ar[i][j] + v
            elif i == len(ar) - 1:
                v = max(dp[i][j-1], dp[i-1][j-1])
                dp[i][j] = ar[i][j] + v
            else:
                v = max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1])
                dp[i][j] = ar[i][j] + v

    max_val = 0
    for i in range(m):
        max_val = max(dp[i][n-1], max_val)

    return max_val 


ar = [
    [10, 33, 13, 15],
    [22, 21, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 14, 2],
]

print(gold_mining(ar, 4, 4))