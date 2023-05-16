set1 = {1,2,2,3,3,3,4}
print(set1)
print(len(set1))

set2 = set('helllllllo')
print(set2)

set3 = set([1,1,1,1,2,2,2,3,3,4]) #列表转换为集合
print(set3)

set4 = {num for num in range(1,20) if num % 3 ==0 or num % 10 == 0}
print(set4)
#生成式语法创建字典

for elem in set4:
    print(elem)