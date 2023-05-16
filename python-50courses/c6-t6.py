#计算最大公约数和最小公倍数
x = int(input("x="))
y = int(input("y="))
for factor in range(x, 0, -1):   #factor从x-0依次递减的取值数
    if x % factor == 0 and y % factor ==0:  #看除后是否有余数，两者都无余数，则说明factor是公因数
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break

#factor n.因子    