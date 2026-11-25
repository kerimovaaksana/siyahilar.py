# siyahilar ve ya list tipi

number = 5.6
print(type(number))
words = "alpha"
print(type(words))
list1 = []
print(type(list1))

lst1 = [2, -5.6 , "alma", -6, 13]
letters = "abcd"
print(letters[2])
print(lst1[2])

# siyahi metodlari
# 1.append(element) - siyahinin sonuna verilmis elementi elave edir
lst1.append(19)
lst1.append(2.5)
lst1.append("apple")
print(lst1)

# 2.insert(index, element) - necenci indekse element elave etmek ucun 
lst1.insert(2, 70)
lst1.insert(4, 100)
print(lst1)

# 3.extend(siyahi) - bir siyahini basqa siyahinin sonuna elave edir
a = [2, 4, 6]
b = [1, 3, 5]
# a.append(b)
# print(a)
a.extend(b)
print(a)

# 4.remove(element) - verilmis elementi siyahidan silir
a.append(4)
a.remove(4)
print(a)

# 5.pop(index) - verilmis indeksdeki elementi silir ve hemin elementi qaytarir
# eger index gosterilmese sonuncu indeksi silir
c = [10, 20, 30, 40]
c.pop(1)
c.pop()
print(c)

# 6.clear() - siyahinin icini bosaldir
# c.clear()
# print(c)

# 7.del() - siyahini legv edir yaddasdan
# del(c)
#print(c)

# 8.count(element) - verilmis element siyahida nece saydadir
d = [3, 5, 6, 3, 5, -3, 8.6]
print(d.count(3))

# 9.sort() - verilmis siyahini siralayir
d.sort()
print(d)

# 10. reverse() - verilmis siyahini tersine siralayir
d.reverse()
print(d)