# 创建一个函数，除去字符串前面和后面的空格

def clear_blank_space():
    str = '  What is your favorite color?  '
    str = str.strip()
    print(str)

clear_blank_space()

# 输入一个字符串，判断是否为回文


# 给出一个整型值，能够返回该值的英文，例如输入89，返回eighty-nine，限定值在0~100
def change_number_english():
    num_input = input('输入0-100之间的整数：\n')
    # 把数字和英文对应关系记录在字典中
    dict_num = {0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine'}

    # 把用户输入的数字拆开放入列表
    # list1 = [num_input for i in range(len(num_input))]
    list1 = []
    for i in range(0, len(num_input)):
        list1.append(num_input[i])
    # 把对应的value放入列表
    list2 = []
    for i in list1:
        list2.append(dict_num[int(i)])

    print('-'.join(list2))

change_number_english()

# TODO 加上闰年的判断
# 给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数
# 思路：分别计算该日期是一年中的第几天，再进行比较
# 先假设都是平年，一年365天

import datetime

# 将12个月的天数放进元组中
date_tuple = (31,28,31,30,31,30,31,31,30,31,30,31)
# 将用户输入的日期格式化
def change_date(date):
    return datetime.datetime.strptime(date, '%m/%d/%Y')
# 分别获取年、月、日
def get_year(date1):
    year = date1.year
    month = date1.month
    day = date1.day
    return year,month,day
# 处理数据
def get_date(date1,date2):
    year1,month1,day1 = get_year(date1)
    year2,month2,day2 = get_year(date2)
    # 将输入月份之前的月份的总天数+输入的日期+年份*365天=总的天数
    days1 = sum(date_tuple[:month1-1]) + day1 + (year1-1)*365
    days2 = sum(date_tuple[:month2-1]) + day2 + (year2-1)*365
    # print('你输入的第一个日期{0}总共有{1}天'.format(date1_input,days1))
    # print('你输入的第二个日期{0}总共有{1}天'.format(date2_input,days2))
    if days1>days2:
        print('你输入的第一个日期比第二个日期大{0}天'.format(days1-days2))
    elif days1==days2:
        print('你输入的两个日期相同')
    else:
        print('你输入的第二个日期比第一个日期大{0}天'.format(days2 - days1))

if __name__ == '__main__':
    date1_input = input('请输入一个日期(MM/DD/YYYY):\n')
    date2_input = input('请再次输入一个日期(MM/DD/YYYY):\n')
    date1 = change_date(date1_input)
    date2 = change_date(date2_input)
    get_date(date1,date2)


# 用列表实现栈和队列数据结构
# 栈是只能在一端进行插入和删除，后进先出
# 队列只能在队前删除，队尾插入



# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符
def main():
    str_input = input('请输入一连串单词，以空格隔开：\n')
    # 切片
    list_str = str_input.split()
    str = input('请输入你要查找的单词:\n')
    count = 0
    # 遍历列表，找出目标单词个数
    for i in list_str:
        if i == str:
            count += 1

    print(count)
if __name__ == '__main__':
    main()
