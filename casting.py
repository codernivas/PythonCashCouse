#String and String Function

s = "jerry nivas"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("r"))
print(s.endswith("ED"))
print(s.endswith("as"))
print(s.find("i"))
print(s.find("n", 5))
print(s.replace("s", 'z'))

a = "SHAN"
print("Is Upper : ", a.isupper())
print("Is Upper : ", a.islower())

ga = "Nivas22"
print("Is Alpha Numeric :", ga.isalnum() )
print("Is Alpha :", ga.isalpha())

jn = "he\nis\ngood"
print(jn)
print(jn.splitlines())
print(jn.splitlines(True))

k = "Maths English Tamil Social"
f = "Maths,English,Tamil,Social"
print(k.split(" "))
print(f.split(","))

m = "    Jerry    "
print(len(m))
print(len(m.strip()))
print(len(m.lstrip()))
print(len(m.rstrip()))

l='22-05-1997'
print(l.partition('-'))

#String Manipulation

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