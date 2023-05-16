#定义并使用元组
t1 = (30,10,55) #这是三元组
t2 = ('深圳',40,True,'广东') #这是四元组

print(type(t1),type(t2))  #查看变量类型
print(len(t1),len(t2))  #查看元素数量

# 通过索引运算获取元组中的元素
print(t1[0],t1[-3])
print(t2[3],t2[-1])

# 遍历元组中的元素
for member in t2:
    print(member)

# 成员运算
print(100 in t1)
print(40 in t2)

# 拼接
t3 = t1 +t2
print(t3)

# 切片
print(t3[::3])

# 比较运算
print(t1 == t3)
print(t1 >= t3)
print(t1 < (30,11,55))