"""
将一颗色子掷6000次，统计每个点数出现的次数
"""
import random
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randint(1,6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f"\n1点出现了{f1}次；\
      \n2点出现了{f2}次；\
      \n3点出现了{f3}次；\
      \n4点出现了{f4}次；\
      \n5点出现了{f5}次；\
      \n6点出现了{f6}次。")