students = {
    1001:{'name':"张三",'sex':True,'age':22,'place':'山西大同'},
    1002:{'name':'李四','sex':True,'age':23,'place':'河北保定'},
    1003:{'name':'王五','sex':False,'age':20,'place':'四川广元'}   
}
#字典中嵌套字典

#得到键值对
print(students.get(1002))
print(students.get(1005))
print(students.get(1005,{'name':'无名氏'}))

print(students.keys())
print(students.values())
print(students.items())  #返回键值对
for key,value in students.items():  #对所有键值对进行遍历循环
     print(key,'--->',value)

stu1 = students.pop(1002)  # pop删除相应键值对，并返回该值
print(stu1)
print(len(students))

# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005,{})
print(stu2)

# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
key,value = students.popitem()
print(key,value)

# 如果这个键在字典中存在，setdefault返回原来与这个键对应的值
# 如果这个键在字典中不存在，向字典中添加键值对，返回第二个参数的值，默认为None
result = students.setdefault(1005,{'name':"方启鹤",'sex':True})
print(result)
print(students)


# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
     1005: {'name':"乔峰",'sex':True,'age':32,'place':'北京大兴'},
     1010: {'name':"王语嫣",'sex':False,'age':19},
     1008: {'name':"钟灵",'sex':False,}
}
students.update(others)
print(students)
