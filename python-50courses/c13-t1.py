m = int(input('m='))
n = int(input('n='))

#计算m的阶乘
fm = 1
for num in range(1,m+1):
    fm *= num

#计算n的阶乘
fn = 1
for num in range(1,n+1):
    fn *= num

#计算m-n的阶乘
fk = 1
for num in range(1,m - n + 1):
    fk *= num

print(fm // fn // fk)