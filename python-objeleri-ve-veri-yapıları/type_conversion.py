"""x=input("1.sayı: ")
y=input("2.sayı: ") #Girilen sayılar Str tipinde bu yuzden işlemler için dönüştürme yapıp tekradan ele alman gerek 


print(type(x))
print(type(y))


toplam=int(x)+int(y)

print(type(x))
print(type(y))

print(type(toplam),toplam)
print(x+y)"""

x=5  #int
y =2.5 #float
name ="Çınar" #String --> str
isOnline= True #bool 

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#Type conversion 

""" float to int """
x=float(x)
print(x)
print(type(x))

""" int  to float """
y=int(y)
print(y)
print(type(y))

result =x+y #Float daha baskındır unutma ! 
print(result)
print(type(result))

""" bool to str """

isOnline =str(isOnline)
print(isOnline)
print(type(isOnline))

""" bool to int """

isOnline =int(isOnline)
print(isOnline)
print(type(isOnline))