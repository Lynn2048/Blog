# 数字求和
num1=input("请输入第一个数字：")
num2=input("请输入第二个数字：")
sum=float(num1)+float(num2)
# sum=int(num1)+int(num2)
print("数字{0}和数字{1} 相加起来等于：{2}".format (num1,num2,sum))

# 求平方根
num=float(input("请输入一个数字："))
num_sqrt=num**0.5
# print("数字{0}的平方根是{1}".format(num,num_sqrt))
print(' % 0.0f的平方根为 %0.0f'%(num ,num_sqrt))

# 二次方程
import cmath
a=float(input("请输入a:"))
b=float(input("请输入b:"))
c=float(input("请输入c:"))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("结果为{0}和{1}".format(sol1,sol2))

#计算圆的面积
def circlearea(r):
    PI=3.14
    return PI*(r**2)
print("圆的面积为%0.6f"%circlearea(6))

# 随机数的生成
import random
print(random.randint(0,9))

# 摄氏度转华氏度
celsius = float(input('输入摄氏温度: '))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))

# 交换变量
x=input("输入x值：")
y=input("输入y值：")
x,y=y,x
print("变换后的x值为{}".format(x))
print("变换后的y值为{}".format(y))
# print("变换后的x值为%0.1f"%(x))
# print("变换后的y值为%0.1f"%(y))