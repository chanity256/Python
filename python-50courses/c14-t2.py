def get_suffix(filename,ignore_dot=True):
    '''获取文件后缀名
    param filename 文件名
    param ignore_dot 是否忽略后缀名前面的点
    '''
    pos = filename.rfind('.')
    if pos <= 0:
        return ''
    return filename[pos + 1:] if ignore_dot else filename[pos:]

print(get_suffix('readme.txt'))
print(get_suffix('readme.txt.md'))
print(get_suffix('.readme'))
print(get_suffix('readme.'))
print(get_suffix('readme'))