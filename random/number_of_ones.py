"""
the bitwise and of x with x − 1 differs from x only in zeroing 
out the least significant nonzero bit: subtracting 1 changes 
the rightmost string of 0s to 1s, and changes the rightmost 1 to a 0.
"""
def ones(n):
    w = 0
    while (n):
        w += 1
        print(n)
        n &= n - 1
    return w

ones(89798798)