#tuples and its function

b = [1, 2.5, True, "Jerry"]
print(b)
print(type(b))
print("----------------")
a = (1, 2.5, True, "Jerry")
print(a)
print(type(a))
print(a[1])

c= list(a)
print(c)
c.append("Raja")
print(c)
print(type(c))
a = tuple(c)
print(a)
print(type(a))

for i in a:
  print(i)

if "Raja" in a:
  print("Raja is found")
else:
  print("Not found")
print(len(a))

a = (1,)
print(type(a))
del a
a = (1,2,7,4)
b = (5,6,7,8)
c = a + b
print(c)
print(c.count(7))

a = (1,2,7,4)
b = (5,6,7,8)
c = (a, b)
print(c)
print(c[1])
print(c[0][1])

x = ('Jerry',) * 10
print(x)

a = (1, 2, 7, 4)
print(min(a))
print(max(a))