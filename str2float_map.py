#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def char2num(s):
        return DIGITS[s]
    def fn(x, y):       #计算整数
        return x * 10 + y
    def lfn(x, y):      #计算小数
        return x / 10 + y
    dot = 0     #点的位置
    for ch in s:        #找点
        if ch == '.':
            break
        dot += 1
    Z = s[:dot]     #整数部分
    L = []      #小数部分
    i = 0
    for ch in s[dot + 1:]:
        L.append(s[-1 - i])
        i += 1
    print('Z = ', Z)
    print('L =', L)
    return reduce(fn, map(char2num, Z)) + reduce(lfn, map(char2num, L)) / 10
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')