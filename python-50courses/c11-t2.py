set1 = {11,12,13,14,15}
print(10 in set1)
print(15 in set1)
set2 = {'python','java','go','swift'}
print('ruby' in set2)
print('java' in set2)

set3 = {1, 2, 3, 4, 5, 6, 7}
set4 = {2, 4, 6, 8, 10}

print(set3 & set4) #交集
print(set3.intersection(set4))

print(set3 | set4) #并集
print(set3.union(set4))

print(set3 - set4) #差集
print(set3.difference(set4))

print(set3 ^ set4) #对称差,相当于并集减去交集
print(set3.symmetric_difference(set4))
print((set3 | set4)-(set3 & set4))
