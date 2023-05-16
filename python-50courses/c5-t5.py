a = float(input("请输入a="))
b = float(input("请输入b="))
c = float(input("请输入c="))
if a+b > c and a+c > b and c+b >a:
    peri = a+b+c  #周长
    print("周长：{:.1f}".format(peri))  #  print(f'周长: {peri}')可以达到相同效果
    half = peri / 2
    area = (half * (half - a) * (half - b) * \
            (half - c))** 0.5  #面积公式
    print("面积：{:.1f}".format(area))  #print(f'面积: {area}')可以达到相同效果
else:
    print("不能构成三角形")