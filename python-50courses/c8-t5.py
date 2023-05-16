'''
通过列表list，进行代码重构
c8-t1 -> c8-t5
'''
import random

counters = [0] * 6
for _ in range(6000):
    face = random.randint(1,6)
    counters[face - 1] += 1  #这里的face对应的色子点数，cunters[]和face-1对应
for face in range(1,7):  #色子点数1-6
    print(f'{face}出现了{counters[face - 1]}次')