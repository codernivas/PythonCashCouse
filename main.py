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

#If Statement
i = 1
while i <= 10:
  print(i)
  i += 1
print("-----------------")
print("Even No : ")
n = 20
i = 2
while i <= 20:
  print(i)
  i += 2
