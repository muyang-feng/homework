'''创建一个字典，把字典中的键按照字母顺序显示出来'''
dict1 = {'aa': 1, 'cc': 3, 'bb':2}
keys = dict1.keys()#得到字典里的键
key_sorted = sorted(keys)#--对键按照升序进行排序
print(key_sorted)

'''根据已经排序好的字母的键，显示这个字典中的键和值'''
for i in key_sorted:#--依次将排序后的键值赋予i
    print(i, dict1[i])#--i等于键值，dict1[i]等于内容




'''使用随机数模块生成一个随机数集合A和B，
每个集合是0到9的随机数集合。生成之后显示结果A|B和A&B'''
import random
def set_random():
    List = [] #--定义一个空列表用来存储生成的随机数
    i = random.randint(1, 10) #--生成一个随机数，要生成集合的个数
    for j in range(0, i + 1):
        x = random.randint(0, 9) #--产生0-9之间的随机数
        List.append(x)
    return set(List)

A = set_random()
print(A)
B = set_random()
print(B)
print('交集')
print(A & B)
print('并集')
print(A | B)