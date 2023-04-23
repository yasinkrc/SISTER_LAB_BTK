# def changeName(n):
#     n='ada'


# name="yiğit"

# changeName(name)

# print(name) #Çünkü referans tipli değil

# def change(n) :

#     n[0] ="istanbul"

# sehirler =["ankara","izmir"]

# n =sehirler[::]

# n[0] ="istanbul"

# change(n)

# print(sehirler) #--> bunun nedeni list referans değerlidir 
# print(n)
"""  Dikkat sum() fonkisyonu topla işlemi yapıyor ama burada verilen değerler de ilave olarak bir kapalı bir parantez alması gerek """
# def add(a,b) :
#     return sum((a,b))

# print(add(30,4))

# def add(a,b,c=0) :
#     return sum((a,b,c))  

# print(add(30,4,40))

# def add(a,b,c=0, d=0 ,e=0) :
#     return sum((a,b,c,d))

# print(add(30,4,50,40))

# def add(a,b) :
#     return sum((a,b))

# def add(a,b) :
#     return sum((a,b))


# def add(*params): #--> list olarak alınıyordu hatılıyorsan 
#     print(type(params))
#     return sum(params)


# print(add(1,2,3,4,5))


# def add(*params): #--> verdiğimiz veriler farklı olabilir 
#     sum=0
#     for n in params :
#         sum +=n
#     return sum

# print(add(1,2,3,4,5))
# print(add(1,2,3,4,5,5,3,4,4,1,6,4))
# print(add(1,2,3,4,5,6,4,6,46,4,5))

def displayUser(**args):
    print(type(args))
    for key , value in args.items() :
        print("{} is {}".format(key,value))


displayUser(name="Çınar",age=2 ,city="istanbul")

displayUser(name="Ada",age=12 ,city="kocaeli",phone="123456789")

displayUser(name="Yiğit",age=12 ,city="Ankara",phone="123456789",email="yazgulu123@gmail.com")


def myFunc(a,b,*args,**kwargs):
  print(a)
  print(b)
  print(args)
  print(kwargs)



myFunc(10,20,30,40,50,key1="value1",key2="value2")