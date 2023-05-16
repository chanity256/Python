a = '人民'
b = a.encode('UTF-8')
c = a.encode('gbk')
print(b,c)
print(b.decode('utf-8'))
print(c.decode("gbk"))