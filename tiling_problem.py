"""

    PROBLEM DESCRIPTION
        Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. 
        A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

        Eg,
            For a 2 x 4 board, there are 3 ways
                1, All 4 vertical
                2, All 4 horizontal
                3, 2 vertical and 2 horizontal

                * * * *
                * * * *

    SOLUTION
        Let “count(n)” be the count of ways to place tiles on a “2 x n” grid, we have following two ways to place first tile. 
            1) If we place first tile vertically, the problem reduces to “count(n-1)” 
            2) If we place first tile horizontally, we have to place second tile also horizontally. So the problem 
            reduces to “count(n-2)” 
        Therefore, count(n) can be written as below. 
            count(n) = n if n = 1 or n = 2
            count(n) = count(n-1) + count(n-2)

"""

def recursive_tiling(n):
    if n == 1 or n == 2:
        return n
    return recursive_tiling(n-1) + recursive_tiling(n-2)


def tiling(n):
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b, a+b

    return b

print(recursive_tiling( 5 ))
print(tiling( 5 ))
