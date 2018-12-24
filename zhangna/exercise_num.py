import math
import random
# 使用循环和算数运算，生成0到20的奇数
for i in range(21):
    if (i % 2 != 0):
        print(i)

# 使用循环和算数运算，生成0到20的偶数
for i in range(21):
    if (i % 2 == 0):
        print(i)

# 计算正方形面积、计算圆的面积、计算立方体体积
side = int(input("正方形的边长是："))  # 正方形的边长
square_area = side ** 2  # 正方形的面积
r = int(input("圆的半径是："))  # 圆的边长
ciecle_area = r ** 2 * math.pi  # 圆的面积
L = int(input("立方体的边长是："))  # 立方体的边长
cube_area = L ** 3  # 立方体的体积
print("正方形的面积是：{0}" .format(square_area))#{0}是占位符，把.format(square_area)传入{0}当中
print("圆的面积是:{0}".format(ciecle_area))
print("立方体的体积是:{0}" .format(cube_area))

# 写一个函数，判断一个整数是否被另外一个整数整除
def divisible():  # 定义整除函数
    num_a = int(input("num_a="))
    num_b = int(input("num_b="))
    if num_a % num_b == 0:
        print("num_a能够被num_b整除")
    else:
        print("num_a不能被num_b整除")


divisible()

#判断一个数字是否为素数
n = int(input('请输入n的值(大于2):'))
for i in range(2, n):
    if n % i == 0:#n/i的余数等于0
        print("%d不是素数" % n)#%d是打印整数，%s打印字符串，%f打印浮点数
        break
    if n == i + 1:
        print("%d是素数" % n)
        break

'''生成一个有N个元素的由随机数n组成的列表
其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）
然后再随机从这个列表中取X（1<=X<=100）个 随机数出来，对它们排序，然后显示这个子集。'''

