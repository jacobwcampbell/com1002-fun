def hcf(a, b):
    # highest common factor
    if a < b:
        # switch a and b if b is larger
        temp = a
        a = b
        b = temp

    r = -1
    while r != 0:
        r = a % b
        a = b
        b = r
    
    return a

def gcd(a, b):
    # gcd and hcf are equivalent
    return hcf(a, b)

def lcm(a, b):
    return abs(a*b)/gcd(a,b)

def iscoprime(a, b):
    return True if hcf(a,b) == 1 else False
    

def linear_diophantine_simple(a, b, c, n):
    # ax + by = c
    # check whether solutions exist
    # calculate base solutions
    # return list of n solutions if they exist
    pass

