def normalize(name):
    name = name.lower()
    l = list(name)
    l[0] = l[0].upper()
    s = ''.join(l)
    return s
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)