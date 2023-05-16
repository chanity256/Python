"""
找出水仙花数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身
"""
for num in range(100,1000):  #把数字范围卡在100-999的三位数中
    low = num % 10  #取得个位数
    mid = num // 10 %10 #取得十位数376 // 10 == 37，37 % 10 ==7
    high = num // 100  #取得百位数
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
