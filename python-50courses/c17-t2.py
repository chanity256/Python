class student:
    #初始化方法
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')

stu1 = student('luohao',40)
stu2 = student('wangdachui',15)
stu1.study('python程序设计')
stu2.play()
