set1 = {"java",'python','go','kotlin'}
set2 = {'kotlin','swift','java','objective-c','dart'}
set3 = {'html','css','javascript'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
# 判断两个集合有无相同元素


set5 = frozenset({1,3,5,7})
set6 = frozenset(range(1,6))
print(set5 & set6)
print(set5 | set6)
print(set5 - set6)
print(set5 ^ set6)
print(set5 < set6)