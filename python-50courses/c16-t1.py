import random
import time

def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2,6))
    print(f'{filename}下载完成.')

def upload(filemname):
    print(f'开始上传{filemname}.')
    time.sleep(random.randint(4,8))
    print(f'{filemname}上传完成.')

download('mysql从删库到跑路.avi')
upload('python从入门到住院')
