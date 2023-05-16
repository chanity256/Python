person = dict(name='wangdachui',age='25',weight='140',home='earth')
print(person)
#dict语法构造字典

#zip压缩2个序列生成字典
items1 = dict(zip('abcde','12345'))
print(items1)
items2 = dict(zip('abcde',range(1,10)))
print(items2)

itmes3 = {x : x**3 for x in range(1,6)}
print(itmes3)

person = {'name':'wangdachui','age':55,'weight':60,'office':'earth'}
print(len(person))
for key in person:
    print(key)