"""
    N'th CATALAN NUMBER

    PROBLEM DESCRIPTION
        Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
            1) Count the number of expressions containing n pairs of parentheses which are correctly matched. 
            For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

            2) Count the number of possible Binary Search Trees with n keys (See this)

            3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either 
            two children or no children) with n+1 leaves.

            4) Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that 
            no 2 chords intersect.
        
        The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

    ALGORITHM
        Recursive formula:
            C(n+1) = sum( [ C(i) * C(n-i) for i in range(0, n) ] ), { C(0) = 1 }
        
        Dynamic Approach:
            dp_table = [ C(0), C(1), C(2), .... C(n) ]
              use bottom up approach and use the low values stored in table for finding higher values
              Time complexity = O( n^2 )
              Space complexity = O( n )

        Using Formula:
            C(n) = fact( 2*n ) / ( fact( n + 1 ) * fact( n ) )
            simplified to mul(n+2, 2*n) / fact(n) where mul(a, b) = a * (a+1) * (a+2) * .... * (b-1) * b , a > b

            Time Complexity = O( n )
            Space Complexity = O( 1 )

"""


def recursive_catalan(n):
    if n == 0:
        return 1
    else:
        C = recursive_catalan
        return sum([ C(i) * C(n-i-1) for i in range(0, n) ])

# print( recursive_catalan( int(input()) ) )


def dp_catalan(n):
    dp = [1]
    for i in range(1, n+1):
        ci = 0
        for j in range(0, i):
            ci += dp[j] * dp[i-j-1]
        dp += [ci]
    return dp[-1]

# print( dp_catalan( int(input()) ) )


def formula_catalan(n):

    def fact(n):
        if n <= 1:
            return 1
        f = 1
        for i in range(2, n+1):
            f *= i
        return f

    def mul(a, b):
        m = 1
        for i in range(a, b+1):
            m *= i
        return m

    return mul(n+2, 2*n) // fact(n)

print( formula_catalan( int(input()) ) )

