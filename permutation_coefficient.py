"""

    PERMUTATION COEFFICIENT

    PROBLEM DESCRIPTION
        Permutation refers to the process of arranging all the members of a given set to form a sequence. The number 
        of permutations on a set of n elements is given by n! , where “!” represents factorial.
        
        The Permutation Coefficient represented by P(n, k) is used to represent the number of ways to obtain an ordered 
        subset having k elements from a set of n elements.

        Recurrence formula:
            nPr = P(n, k) = P(n-1, k) + k* P(n-1, k-1) , { if k > n => P(n, k) = 0; }

        Formula:
            P(n, k) = fact(n) / fact(n-k)

"""


def permutation_recursive(n, k):
    if k > n or n < 0:
        return 0

    elif n == 1:
        return 1

    P = permutation_recursive
    return P(n-1, k) + k * P(n-1, k-1)


def permutation_dp(n, k):
    dp = []

    for i in range(n):
        row = [0]
        for j in range(1, k+2):
            if j > i+1:
                row += [0]
            elif i == 0:
                row += [1]
            else:
                j -= 1
                row += [ dp[j] + j * dp[j-1] ]
        dp = row

    print(dp)
    return dp[-1]


# print( permutation_recursive(2, 1) )
print( permutation_dp(6, 2) )