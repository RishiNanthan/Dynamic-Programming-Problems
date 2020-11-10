"""
    PROBLEM STATEMENT

        Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
        The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.
        Given a number n, the task is to find n’th Ugly number.

    ALGORITHM

    initialize
    
    ugly[] =  | 1 |
    i2 =  i3 = i5 = 0;

    First iteration
    ugly[1] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
                = Min(2, 3, 5)
                = 2
    ugly[] =  | 1 | 2 |
    i2 = 1,  i3 = i5 = 0  (i2 got incremented ) 

    Second iteration
        ugly[2] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
                = Min(4, 3, 5)
                = 3
        ugly[] =  | 1 | 2 | 3 |
        i2 = 1,  i3 =  1, i5 = 0  (i3 got incremented ) 

    Third iteration
        ugly[3] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
                = Min(4, 6, 5)
                = 4
        ugly[] =  | 1 | 2 | 3 |  4 |
        i2 = 2,  i3 =  1, i5 = 0  (i2 got incremented )

    Fourth iteration
        ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
                = Min(6, 6, 5)
                = 5
        ugly[] =  | 1 | 2 | 3 |  4 | 5 |
        i2 = 2,  i3 =  1, i5 = 1  (i5 got incremented )

    Fifth iteration
        ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
                = Min(6, 6, 10)
                = 6
        ugly[] =  | 1 | 2 | 3 |  4 | 5 | 6 |
        i2 = 3,  i3 =  2, i5 = 1  (i2 and i3 got incremented )

    Will continue same way till I < 150

"""


def ugly(n):
    ar = [1]

    i2 = i3 = i5 = 0
    for i in range(n-1):
        v2 = ar[i2] * 2
        v3 = ar[i3] * 3
        v5 = ar[i5] * 5

        if v2 < v3 and v2 < v5:
            i2 += 1
            ar += [v2]
        elif v3 < v2 and v3 < v5:
            i3 += 1
            ar += [v3]
        else:
            i5 += 1
            ar += [v5]

    return ar[-1]

print( ugly( int(input()) ) )
