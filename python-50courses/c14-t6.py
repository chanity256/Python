#求最大公约数和最小公倍数
def gcd(x:int,y:int) -> int:
    #求最大公约数
    while y % x != 0:
        x, y = y % x, x
    return x

def lcm(x:int,y:int) -> int:
    return x * y // gcd(x,y)
#求最小公倍数
