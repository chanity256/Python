import random
import string

ALL_CHARA = string.digits + string.ascii_letters

def generate_code (code_len=4):
    '''生成指定长度的验证码'''
    return ''.join(random.choices(ALL_CHARA,k=code_len))

for _ in range(10):
    print(generate_code())
# 随机产生10组验证码