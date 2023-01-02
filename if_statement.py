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