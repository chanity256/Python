#用户身份验证
username = input("请输入用户名：")
password = input("请输入口令：")
if username == "admin" and \
    password == "111111":
    print("身份验证成功！")
elif username != "admin" and \
    password == "111111":
    print("用户名错误！")
elif username == "admin" and \
    password != "111111":
    print("密码错误！")
else:
    print("用户名和密码错误！")