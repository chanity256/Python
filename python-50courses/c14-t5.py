def gcd_and_lcm(x:int,y:int) -> int:
    a,b = x,y
    while b % a != 0:
        a,b = b % a,a
    return a,x * y //a