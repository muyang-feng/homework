# # 使用循环和算数运算，生成0到20的偶数
# for i in range(20):
#     if i%2 == 0:
#         print('%d是0-20的偶数'% i)
#
# print()
#
#
# # 使用循环和算数运算，生成0到20的奇数
# for i in range(0,20):
#     if i%2 != 0:
#         print('{0}是0-20的奇数'.format(i))
#
# # 计算正方形，长方形，圆面积；计算立方体体积
#
# import math
# side_square = float(input('请输入正方形的边长(cm)：\n'))
# area_square = side_square ** 2
# bulk_square = side_square ** 3
# print('正方形的面积为：%d' % area_square)
# print('正方体的体积为：{0}'.format(bulk_square))
# print()
#
# long_rectangle = float(input('请输入长方形的长(cm)：\n'))
# wide_rectangle = float(input('请输入长方形的宽(cm)：\n'))
# high_rectangle = float(input('请输入长方体的高(cm)：\n'))
# area_rectangle = long_rectangle * wide_rectangle
# bulk_rectangle = long_rectangle * wide_rectangle * high_rectangle
# print('长方形的面积为:{0}'.format(area_rectangle))
# print('长方体的体积为:{0}'.format(bulk_rectangle))
# print()
#
# radius = float(input('请输入圆的半径(cm)：\n'))
# high_round = float(input('请输入圆的高(cm):\n'))
# area_round = round(math.pi,2)* radius ** 2 # 取两位小数
# bulk_round = area_round * high_round
# print('圆的面积为：{0}'.format(area_round))
# print('圆柱体的体积为：%s'% bulk_round)
#
# # 写一个函数，判断一个整数是否被另外一个整数整除
# def main():
#     a = int(input('输入整数a:'))
#     b = int(input('输入整数b:'))
#     if a % b == 0:
#         print('{0}能被{1}整除'.format(a,b))
#
# main()
#
# # 判断一个数字是否为素数（只能被1和本身整除的数）
# num = int(input('请输入一个数：'))
# for i in range(2,num):
#     if num % i == 0:
#         print('%d不是一个素数' % num)
#         break
#     else:
#         print('%d是一个素数' % num)
#         break
#
#
# '''
# 生成一个有N个元素的由随机数n组成的列表，
# 其中N和n的取值范围分别为（1< N <= 100）和（0<=n<=2**31 -1）。
# 然后再随机从这个列表中取x（1<=x<=100）个 随机数出来，
# 对它们排序，然后显示这个子集。
# '''
import random
# 生成一个有N个元素的由随机数n组成的列表
list_n = [random.randint(0,31**2-1) for i in range(random.randint(1,100))] # 列表推导式
print(list_n)
# 随机从上面列表中取x（1<=x<=100）个 随机数
list_x =[]
for i in range(random.randint(1,100)):
    list_x.append(list_n[random.randint(1,len(list_n)-1)])
print(list_x)
# 升序排列
list_x.sort()
print(list_x)

'''
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
你可以假设每种输入只会对应一个答案。
但是，你不能重复利用这个数组中同样的元素。 
示例: 给定 nums = [2, 7, 11, 15], target = 9 因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]
'''
