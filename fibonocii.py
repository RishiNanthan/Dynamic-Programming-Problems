"""
    PROBLEM STATEMENT
        The Fibonacci numbers are the numbers in the following integer sequence.
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
        In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
            F(n) = F(n-1) + F(n-2) , { F[0] = 0, F[1] = 1 }

    ALGORITHM
        Using bottom-up approach, we can store f0, f1, f2, f3... in an array from which next value can be calculated by
        adding previous 2 values of the array ie., f4 = f2 + f3 

"""


def fibonocci(n):

    fib = [0, 1]

    if n <= 2:
        return fib[n-1]

    for i in range(n-2):
        fib = fib[1], (fib[0] + fib[1])

    return fib[1]


print( fibonocci( int(input("N: ")) ) )