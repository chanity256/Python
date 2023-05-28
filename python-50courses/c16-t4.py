def fib(n):
    if n in (1,2):
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1,21):
    print(fib(i))

#得到前20个斐波那契数列