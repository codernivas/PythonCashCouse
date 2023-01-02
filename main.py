#Basic
'''
a=10
b=5
c=a+b
print(c)
'''

#Getting values from user as input
'''
#string Method

a=input("Enter A value : ")
b=input("Enter B value : ")

print(a)
print(b)

print(type(a))

#integer Method , float Method

#value1=int(input("Enter Value1 : "))
#value2=int(input("Enter Value2 : "))

value1=float(input("Enter Value1 : "))
value2=float(input("Enter Value2 : "))

print(value1)
print(value2)

Total=value1+value2
print("Total value is : ",Total)

print(type(Total))
'''

#Multiple inputs in single line

'''name1,name2=input("Enter 2 names : ").split(',')
print("Name1 is :", name1)
print("Name2 is :", name2)'''

#list
'''
para=["10","2","60"]
print(para[1])

print(",".join(para))
'''

#Multi line input like paragraph
'''
para=[]
print("Enter a text ")

while True:
  line=input()
  if line:
    para.append(line)
  else:
    break

print(para)

output='\n'.join(para)
print(output)
'''

#Casting Type

'''
 s  a  m  p  l  e
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
'''
s="sample"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])
