#class

class Person : #Genelde büyük harfle başlar
     # pass--> yer tuttucudur
    address="no information"
    # class attributes

    #constructor (yapıcı method)
    def __init__(self,x ,y):
    #Object attributes
     self.name=x
     self.year=y
     print("init metodu çalıştı ")
    #instance methods
   
# if a >5 :
#     pass


# object (instance)

p1=Person('yasin',1555)
p2=Person('yazgülü',1970)

#updating
p1.name="ahmet"
p1.year=1245


# accessing object attribues
print(f"name : {p1.name} , year : {p1.year} adress : {p1.address}")
print(f"name : {p2.name} , year : {p2.year} adress : {Person.address}")

print(p1)
print(p2)

print(type(p1))
print(type(p2))
print(p1==p2)