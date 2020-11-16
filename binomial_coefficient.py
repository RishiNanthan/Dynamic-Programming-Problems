"""
    BINOMIAL COEFFICIENT

    PROBLEM DESCRIPTION
        A binomial coefficient C(n, k) can be defined as the coefficient of x^k in the expansion of (1 + x)^n.
        A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen 
            from among n objects more formally, the number of k-element subsets (or k-combinations) of a n-element set.
            also commonly known as nCr

        Recursive Formula:
            C(n, k) =  C(n-1, k-1) + C(n-1, k), { C(n, 0) = C(i, i) = 1 }

        Formula:
            C(n, k) = fact(n) / ( fact( n-k ) * fact( k ) )

"""


def binomial_recursive(n, k):
    if k == 0 or n == k:
        return 1
    C = binomial_recursive

    return C(n-1, k-1) + C(n-1, k)


def binomial_dp(n, k):
    dp = []
    for i in range(n):
        row = []
        for j in range(k+1):
            if j > i+1:
                break
            elif j == 0 or i+1 == j:
                row += [1]
            else:
                row += [ dp[-1][j-1] + dp[-1][j] ]

        dp += [row]
    print(dp)
    return dp[-1][-1]


def binomial_formula(n, k):

    def fact(m):
        f = 1
        for i in range(2, m+1):
            f *= i
        return f
    
    return fact(n) // ( fact(n-k) * fact(k) )



# print( binomial_recursive(5, 2) )
# print( binomial_dp(5, 2) )
print( binomial_formula(5, 2) )

