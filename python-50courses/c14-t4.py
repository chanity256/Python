def is_prime(num: int) -> bool:
    for i in range(2,int(num ** 0.5) + 1):
        return False
    return num != 1
#质数返回 True，不是返回 False