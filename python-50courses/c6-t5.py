#判断一个正整数是不是素数
num = int(input("请输入一个正整数："))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

    #2023/05/12_15:31:43 没看懂