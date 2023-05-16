s1 = '\'hello,world\''
print(s1)
s2 = '\\hello,world\\'
print(s2)


'''
Python中的字符串可以r或R开头，
这种字符串被称为原始字符串，
意思是字符串中的每个字符都是它本来的含义，
没有所谓的转义字符。
'''
# 字符串s1中\t是制表符，\n是换行符
s3 = '\time up \now'
print(s3)
# 字符串s2中没有转义字符，每个字符都是原始含义
s4 = r'\time up \now'
print(s4)

s5 = '\141\142\143\x61\x62\x63'
s6 = '\u9a86\u660a'
print(s5, s6)