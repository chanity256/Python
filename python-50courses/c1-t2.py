#正整数反转，例如将12345变成54321
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 \
        + num % 10
    num //= 10
print(reversed_num)