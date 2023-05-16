import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a),sys.getsizeof(b))

print(timeit.timeit('[1,2,3,4,5,6,7,8,9]'))
print(timeit.timeit('(1,2,3,4,5,6,7,8,9)'))
#通常不可变类型在创建时间和占用空间上面都优于对应的可变类型。