items = ['python','java','java','go','kotlin','python']

#查找元素的索引位置
print(items.index('python')) #第一个‘python’出现的索引
print(items.index('python',2)) #第二个‘python’出现的索引
print(items.index('java',3)) # 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的

print(items.count('python'))
print(items.index('java'))
print(items.count('swift'))