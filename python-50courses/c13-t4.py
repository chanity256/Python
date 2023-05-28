def add(*args):
    total = 0
    for val in args:
        if type(val) in (int,float):
            total += val
    return total
    
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))