#生成式创建列表,比较和c8-t9的区别。明显此方法更加优雅简单
items1 = [x for x in range(1,10)]
itmes2 = [x for x in 'hello world' if x not in 'aeiou']
items3 = [x + y for x in 'abc' for y in '123']

print(f'{items1}\n\r{itmes2}\n\r{items3}')