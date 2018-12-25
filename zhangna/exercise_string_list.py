#1.创建一个函数，除去字符串前面和后面的空格
def blank():
    strl = '  aa  bb  cc  '
    print(strl)
    str2 = strl.replace(" ", "")
    print(str2)

blank()

# 2.输入一个字符串，判断是否为回文
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
single = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
double = ['ten', 'eleven', 'tweleve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seveteen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
numstr = input('请输入一个数字，范围在0-100: ')
numlen = len(numstr)
num = int(numstr)
print(num)
if numlen == 1:
    if int(numstr[0]) > 0:
        print(single[num])
    else:
        print('zero')
elif numlen == 2:
    if numstr[0] == '1':
        print(double[num - 10])
    else:
        print(tens[int(numstr[0])] + '-' + single[int(numstr[1])])
elif numlen == 3:
    print('one hundred')


'''给出两个可以识别格式的日期，比如MM/DD/YY 或者 DD/MM/YY 计算两个日期的相隔天数'''


