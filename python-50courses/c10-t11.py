s = 'I#love#you#so#much'
words = s.split('#')
print(words)
words = s.split('#',3)
print(words)

#而且还可以指定最大拆分次数来控制拆分的效果。本次指定最大拆分是3次