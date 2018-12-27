#创建一个字典，把字典中的键按照字母顺序显示出来
dict1 = {'b':98,'a':97,'d':100,'c':99}
list_key = sorted(dict1.keys())
print(sorted(list_key))

#根据已经排序好的字母的键，显示这个字典中的键和值
list_value = []
for i in list_key:
    list_value.append(dict1[i])
print(list_value)


dict1 = {'a':97,'b':98,'c':99,'d':100}
keys = dict1.keys()
values = dict1.values()
print(keys)
print(values)
print(dict1.items())

#使用随机数模块生成一个随机数集合A和B，每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B
import random
A = {random.randint(0,9)}
print(A)
B = {random.randint(0,9)}
print(B)
print(A|B)
print(A&B)
