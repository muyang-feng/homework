#1,生成0-20的偶数
# a = 22
# while a > 0:
#     a = a - 2
#     print(a)


#2,生成0-20的奇数

# b = 21
# while b > 1:
#     b -= 2
#     print(b)

#3,计算长方形
# a = input('长')
# b = input('宽')
# c = int(a)
# d = int(b)
# e = c * d
# print(e)

#4,计算圆的面积
# import math
# r=float(input('半径：'))
# area=math.pi*r*r
# print ( "圆的面积:% 2f"% area)


#5,立方体体积公式
# a = int(input('长'))
# b = int(input('宽'))
# c = int(input('高'))
# c = a * b * c
# print(c)


#6,判断一个数是不是素数
# a = int(input("输入一个数"))
# if a<=1:
#     print("不是素数")
# elif a == 2:
#     print("是素数")
# else:
#     b = 2
#     while b < a:
#         if a % b ==0:
#             print("不是素数")
#             break
#         b = b + 1
#     else:
#      print("是素数")

#7,一个数能不能被另一个数整除
# in_t = input()
# [a , b] = in_t.split()
# if int(a) % int(b) ==0:
#     print("能整除")
# else:
#     print("不能整除")

#8,创建函数去掉行首尾空格----操作不出来
# def s ( a):
#     b = a.strip()
#     return b
#
# c = s(" kkkk ")
# print(c)

# 9, 输入一个字符串，判断是否为回文
# s_t = str(input(">>>"))
# a = s_t[:1]
# b = s_t[-1:]
# if a == b:
#     print("是回文")
#  else:
#     print("不是回文")

#10,数值翻译成英文
# a = int(input(">>>>>>>>"))
# d1 ={ 0:"zero ", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
#       8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
#       14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
# d2 =  {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
#
# if a >= 20:
#     if 0 == a % 10:
#             print(d2[a / 10])
#     elif a % 10 > 0:
#             print(d2[a // 10],d1[a % 10])
# elif a >= 0:
#         print(d1[a])


# 11栈和队列
# # a = [1,2,3]
# # #栈的实现：后进先出
# # a.append()#最后增加
# # a.pop()#删除最后
# 队列：先进先进先出
# a.append()
# a.pop(0)#删除第一个


#12,统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符
# a = " is the premier online source of Guangdong news and information, fully "
# c =a.split()
# print(c)




#13,创建一个字典，把字典中的键按照字母顺序显示出来
#键顺序显示
# a = { "a" : 1, "c" : 9,"b":6}
# b = sorted(a)
# print(b)
#按键顺序显示对应的值
# d =sorted(zip(a.keys(),a.values()))
# print(d)

#使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
# import random
# a = random.randint(0,9)
# d = []
# for i in range(0,a):
#     c = int(random.randint(0,9))
#     d.append(c)
#     A = list(set(d))
# print(A)
#
# a1 = random.randint(0,9)

# d1 = []
# for i in range(0,a1):
#     c1 = int(random.randint(0,9))
#     d1.append(c1)
#     B = list(set(d1))
# print(B)
# print(list(set(A) &set(B)))