# Задание - 1 
#l = [1, -2, 'a', 1.2]
#print(list(filter(lambda x: type(x) == int and not x&1, l)))

# Задание - 2
#l = [1, -2, 'a', 1.2]
#print(l[::2]) # or print(l[0:len(l) - 1:2])

# Задание - 3
#l = [1, -2, 'a', 1.2]
#print(list(filter(lambda x: (type(x) == int or type(x) == float) and x >= 0 , l)))

# Задание - 4

#l = [1, 3, 4, 7, 9, 11]
#m = 3

#def f(lst, m):
#    tmp, res = [], []
#    for x in lst:
#        rem = x % m
#        for y in lst:
#            if (y % m == rem):
#                tmp.append(y)
#        res.append(tmp[:])
#        tmp.clear()

#    for x in res:
#        if x not in tmp:
#            tmp.append(x)
#    return tmp

#def F(lst, m):
#    tmp, res = set(), []
#    for x in lst:
#        rem = x % m
#        for y in lst:
#            if (y % m == rem):
#                tmp.add(y)
#        res.append({*tmp})
#        tmp.clear()
    
#    l.clear()
#    for x in res:
#        if x not in l:
#           l.append(x)
   
#    return l

#print(F(l,m))

# Задние - 5

#d = {1:2, 'a':3, -1:1, 3:'a'}

#def f(dic):
#    sum = [0,0]
#    for x in dic:
#        if((type(dic.get(x)) == int or type(dic.get(x)) == float) and (type(x) == int or type(x) == float)):
#            sum[0] += dic.get(x)
#            sum[1] += x
#    return sum

#print(f(d))

# Задние - 6

#l = [3, 4.1, 2]

#def check(lst):
#    s = []
#    for x in lst:
#        for y in lst:
#            try:
#                if x < y: s.append((x, y))
#            except TypeError:
#                print('Ограничимся числами')
#    return s

#print(check(l))

# Задание - 7

l = ['a',1,-2,1.2]

def f(lst):
    keys = lst[::2]
    val = lst[1::2]

    for x in val:
        d = dict.fromkeys(keys, x)

    return d

print(f(l))