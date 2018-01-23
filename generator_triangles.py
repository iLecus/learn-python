def triangles():
    t = []      #每级列表
    L = []      #用来储存上一级列表
    n = 0       #列表级数
    while True:     #死循环，根据yeild停止
        i = 1
        while i < n:        #只加到n - 1位
            t[i] = l[i - 1] + l[i]
            i += 1
        t.append(1)     #末尾加1
        n += 1
        l = t[:]
        yield l
    return 0
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')