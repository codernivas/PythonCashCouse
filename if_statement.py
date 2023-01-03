#If statement

n = int(input("Enter the Number : "))
if n % 2 == 0:
  print(n, "is Even Number")

#if else statement

name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))

if age >= 18:
  print(name, "age is", age, "Eligible for Vote")
else:
  print(name, "age is", age, "Not Eligible for Vote")

#elif statement
  
days = int(input("Enter The Days : "))

if days == 0:
  print("Good No Fine")
elif days >= 1 and days <= 5:
  print("Fine Amount :", days * 0.5)
elif days > 5 and days <= 10:
  print("Fine Amount :", days * 0.5)
elif days > 10 and days <= 30:
  print("Fine Amount :", days * 5)
else:
  print("Menbership cancel")


#Nested if

m1 = int(input("Enter Mark-1 : "))
m2 = int(input("Enter Mark-2 : "))
m3 = int(input("Enter Mark-3 : "))

total = m1+m2+m3
average = total/3.0

print("Total : ",total)
print("Average : ",average)

if m1 >= 35 and m2 >= 35 and m3 >=35:
  print("Result : Pass")
  if average >=90 and average <= 100:
    print("Grade : A")
  elif average >= 80 and average <= 89:
    print("Grade : B")
  elif average >= 70 and average <= 79:
    print("Grade : C")
else:
  print("Result :Fail")
  print("Grade :No Grade")

#while loop

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

#Range 

print(list(range(5)))
print(list(range(2,5)))
print(list(range(0,21,5)))
print(list(range(1,20,2)))

#For loop

for i in range(0, 21, 2):
 print(i)

for i in range(5):
  a=int(input("Enter a no : "))
  b=int(input("Enter a no : "))
  print(a+b)

#Nested for

for i in range(6):
  for j in range(i):
    print("*",end="")
  print("")
print("---------------")

for i in range(5,0,-1):
  for j in range(i):
    print("*",end="")
  print("")
print("---------------")

for i in range(65,70,1):
  for j in range(65,70,1):
    print(chr(j),end="")
  print("")

#While else and for else

i=1
while i<=5:
  if(i==4):
    break
  print(i)
  i+=1
else:
  print("Loop completed")

print("-----------------")

for i in range(1,21):
  if i==5:
    break
  print(i)
else:
  print("For Loop Completed")