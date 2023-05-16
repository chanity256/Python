set1 = {1,3,5}
set2 = {1,2,3,4,5}
set3 = set2

# 真子集<  子集<=
print(set1 < set2,set1 <= set2)
print(set2 < set3,set2 <= set3)
print(set1.issubset(set2))

print(set.issuperset(set1))
print(set2 > set1)