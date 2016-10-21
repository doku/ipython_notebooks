def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    from fractions import gcd
    def lcm(x,y):
    	return (x*y)//gcd(x,y)
    #return lcm(a,b)
    
    def gcd(x,y):
        if y > x:
            x, y = y, x
        while y != 0:
            x, y = y, x % y
        return x
    return (a*b) // gcd(a,b)


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    #return len(set(str(n)))
    f = sorted(list(str(n)))
    return len([x for i,x in enumerate(f) if x not in f[i+1:]])
    #print(len(set(str(n))), r)
    
