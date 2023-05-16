person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print('name' in person,'tel' in person)

if 'age' in person:
    person['age'] = 25
#修改键值对

person['tel'] = '1232132342'
person['signature'] = '你的男朋友是一个盖世渣男'
print('name' in person,'tel' in person)
#通过索引向person字典添加新的键值对

print(len(person))
for key in person:
    print(f'{key}: {person[key]}')
# 对字典的键进行循环并通索引运算获取键对应的值