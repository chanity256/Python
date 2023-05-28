def fac(num):
    if num in (0,1): #递归的收敛条件
        return 1
    return num * fac(num - 1) #递归公式