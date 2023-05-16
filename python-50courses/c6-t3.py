#猜数字，while语法
import random

#产生1-100范围内的随机数
answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了！")
        break
print("你总共猜对了：{}次".format(counter))