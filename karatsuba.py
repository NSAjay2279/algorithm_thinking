def kara_mult(x,y):
    if len(str(x))==1 or len(str(y))==1:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        n_half = n//2

        a = x//(10**n_half)
        b = x % (10**n_half)
        c = y//(10**n_half)
        d = y%(10**n_half)


        ac = kara_mult(a,c)
        bd = kara_mult(b,d)
        ad_plus_bc = kara_mult(a+b, c+d) - ac - bd

        product = 10**(2*n_half)*ac + 10**(n_half)*(ad_plus_bc) + bd
        return product


try:
    assert kara_mult(999999, 2) == (999999 * 2)
except AssertionError:
    print("False")
    

