#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: iLecus Time:2018/1/24


def is_palindrome(n):
    s = str(n)
    i, count = 0, 0
    while i < len(s):
        if s[i] == s[-1 - i]:
            count += 1
        i +=1
    if count == len(s):
        return True
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')