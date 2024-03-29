import time
import random
# 定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func):
    
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result
    
    # 返回带装饰功能的wrapper函数
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2,6))
    print(f'{filename}下载完成。')

@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random .randint(4,8))
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')


'''
上面的代码，我们通过装饰器语法糖为download和upload函数添加了装饰器，
这样调用download和upload函数时，会记录下函数的执行时间。
事实上，被装饰后的download和upload函数是我们在装饰器record_time中返回的wrapper函数，
调用它们其实就是在调用wrapper函数，所以拥有了记录函数执行时间的功能。
'''