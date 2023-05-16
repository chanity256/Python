"""
百钱百鸡问题:
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，
问公鸡、母鸡、小鸡各有多少只？
"""
#使用穷举法来解决
#假设公鸡数量x，x取值范围在0-20
for x in range(0,21):
    #假设母鸡的数量为y，y的取值是在0-33
    for y in range(0,34):
        z = 100 - x -y
        if 5 * x + y * 3 + \
            z // 3 == 100 and \
            z % 3 == 0:
            print(f"公鸡：{x}只，母鸡：{y}只，小鸡：{z}只")   
#同时确保，价钱和为100元，且小鸡数目是3的倍数