'''
找到100以内的素数
'''
for num in range(2,100):  #1不是素数，所以从2开始
    #假设num是素数
    is_prime = True
    #在2到num-1之间寻找num的因子
    for factor in range(2,num):
        #如果找了num的因子，那么他不是素数
        if num % factor == 0:
            is_prime = False
            break
        #如果布尔值是True则num是素数
    if is_prime:
         print(num)