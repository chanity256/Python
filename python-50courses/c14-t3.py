'''
直接使用os.path模块的splitext函数，这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，
然后返回一个二元组，二元组中的第二个元素就是文件的后缀名（包含.），
如果要去掉后缀名中的.，
可以做一个字符串的切片操作，代码如下所示。
'''

from os.path import splitext

def get_suffix(filename,ignore_dot=True):
    return splitext(filename)[1][1:]