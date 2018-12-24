#创建一个函数，除去字符串前面和后面的空格
def blank():
    strl = '  aa  bb  cc  '
    print(strl)
    str2 = strl.replace(" ", "")
    print(str2)

blank()

# 输入一个字符串，判断是否为回文
string = input('请输入一个字符串：')
str_len = len(string)
i = 0
while i <= str_len / 2:
    if string[i] == string[str_len-i-1]:
        count=1
        i=i+1
    else:
        count=0
        break

if count==1:
    print('输入的字符是回文')
else:
    print('输入的字符不是回文')

'''给出一个整型值，能够返回该值得英文，例如输入89，返回eighty-nine，限定值在0~100'''


