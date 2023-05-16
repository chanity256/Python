from random import randint

def roll_dice(n=2): #设置默认色子个数为2
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
print(roll_dice()) #摇2颗色子
print(roll_dice(3)) #摇3颗色子

"""
这是c7-t4.py的代码重构
"""