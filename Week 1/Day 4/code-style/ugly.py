def fac(n):
    """
    This is a docstring
    ---
    param(input): integer
    param(output): integer
    """
    step = lambda x: (1 + (x<<2)) - ((x>>1)<<1) # This does something 
    maxq = long(floor(sqrt(n)))
    d = 1
    q = (n % 2 == 0) and 2 or 3
    while (q <= maxq) and (n % q != 0):
        q = step(d)
        d += 1
    return (q <= maxq) and (q + fac(n//q)) or n
