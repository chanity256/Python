s = '   wanghaonan_256@126.com   \t\r\n'
print(s.strip())  # strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.rstrip())
print(s.lstrip())

s = 'hello,world'
print(s.replace('o','$'))
print(s.replace('o','$',1))
#替换操作

s = 'I love you'
words = s.split() #拆分字符串
print(words)
print('#'.join(words)) #合并字符串