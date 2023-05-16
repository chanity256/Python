set1 = set()

# add和update添加元素
set1.add(33)
set1.add(55)
set1.update({1,10,100,1000})
print(set1)

# discard删除指定元素
set1.discard(100)
set1.discard(99)
print(set1)

if 10 in set1:
    set1.remove(10)
print(set1)
# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常

print(set1.pop(),set1)


set1.clear()
print(set1)
