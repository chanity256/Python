class student:

    def study(self,course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')


#以构造器语法来创建对象
stu1 = student()
stu2 = student()
print(stu1)
print(stu2)
print(hex(id(stu1)),hex(id(stu2)))
'''
用print函数打印stu1和stu2两个变量时，
我们会看到输出了对象在内存中的地址（十六进制形式），
跟我们用id函数查看对象标识获得的值是相同的。
'''
student.study(stu1,'python程序设计')
#类.方法 来调用

stu1.study('python程序设计')
#对象.方法 来调用

student.play(stu2)
stu2.play()