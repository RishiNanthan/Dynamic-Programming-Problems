"""
    BELL NUMBER

    PROBLEM DESCRIPTION
        It is the number of ways to partition a set with n elements

        Number of ways to Partition a Set {1, 2, 3} with 3 elements
            partitions = {{1}, {2}, {3}}, {{1, 2}, 3}, {{1, 3}, 2}, {{2, 3}, 1}, {{1, 2, 3}}
            no of partitions = 5

        Recursive formula:
            Bell(n) = sum( [ S(n, k) for k in range(n+1) ] ) ,
                where S(n, k) = k * S(n-1, k) + S(n-1, k-1), { S(0, 0) = 1 ; S(0, i) = S(j, 0) = 0 for all i, j > 0 }

                S(n, k) is called the stirling partition number, it refers to the number of possible partitions of k segments

            How does above recursive formula work?
                When we add a (n+1)’th element to k partitions, there are two possibilities.
                    1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
                    2) It is added to all sets of every partition, i.e., k*S(n, k)
                S(n, k) is called Stirling numbers of the second kind

        First few Bell numbers are 1, 2, 5, 15, 52, 203, ….

        BELL'S TRIANGLE:
            1
            1 2
            2 3 5
            5 7 10 15
            15 20 27 37 52

"""


def stirling_recursive(n, k):
    if n == k:
        return 1
    elif n == 0 or k == 0:
        return 0
    
    return k * stirling_recursive(n-1, k) + stirling_recursive(n-1, k-1)


def bell_recursive(n):
    S = stirling_recursive
    return sum( [ S(n, k) for k in range(n+1) ] )


def bell_using_triangle(n):
    if n == 1 or not n:
        return 1
    pre = [1]
    for i in range(n-1):
        cur = [pre[-1]]
        for i in range(len(pre)):
            cur += [pre[i] + cur[-1]]
        pre = cur
    
    return pre[-1]


# print( bell_recursive( int(input()) ) )
print( bell_using_triangle( int(input()) ) )

