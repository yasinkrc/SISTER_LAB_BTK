# class Person : #Genelde büyük harfle başlar
#     # class attributes
#     address="no information"
    
#     #constructor (yapıcı method)
#     def __init__(self,name ,year):
#         #Object attributes
#         self.name=name
#         self.year=year
     
#     #instance methods
   
#     #methods
#     def intro(self):
#         print("Hello There. I am "+self.name)


#     def calculate(self):
#         return 2019-self.year

# # object (instance)

# p1=Person('yasin',1555)
# p2=Person('yazgülü',1970)

# #updating
# p1.name="ahmet"
# p1.year=1245


# p1.intro()
# p2.intro()

# print(f"adım: {p1.name} ve yaşım : {p1.calculate()}")

# print(f"adım: {p2.name} ve yaşım : {p2.calculate()}")

class Circle :
    #Class object attribute 
    pi=3.14 #--> hepsi için ortak oldu 

    def __init__(self,yaricap=1) :
        self.yaricap=yaricap
    
    def cevreHesapla(self):
        return 2*self.pi +self.yaricap

    def alan_Hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle()

c2=Circle(5)

print(f"c1: alan = {c1.alan_Hesapla()} çevre  = {c1.cevreHesapla()}")

print(f"c2: alan = {c2.alan_Hesapla()} çevre  = {c2.cevreHesapla()}")