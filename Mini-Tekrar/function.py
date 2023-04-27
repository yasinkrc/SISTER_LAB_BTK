#Fonksiyon - parametre - return 

print("Hello python")

# def fun():
#     print("Hello python fonksiyon ")

# fun() #def din altında olması gerekiyor 
# fun() 
# fun() 
# fun() 
# fun() 

# def fun ():
#     print("merhaba")
#     print("yasin")
#     print("nasılsin")

# fun()


# def yazdir(strYazılım):
#     print("Hello {}".format(strYazılım))

# yazdir("python")
# yazdir("java")

# def topla(sayi1 ,sayi2):
#     print(int((sayi1+sayi2)))
# #sum fonkisyonu bir list ,tuple gibi yinelemeli olaylarda kullanılıt 
# topla(4,5)

# def kisi(name , age ,job):
#     print(f"Kişi adı {name} \n Kişinin yaşi {age} \n Kişinin mesleği {job}")

# kisi("Yazgülü",21,"Ergoterapi")

# def num_pow(num1,num2=5):
#     print(num1**num2)

# # num_pow(2,3)
# num_pow(2)

# def num_pow(num1,num2):
#     print("hello world")

# print(type(num_pow)) #function 

# def num_pow(num1,num2):
#      return num1**num2

# print(num_pow(3,4))


def get_greater_num(num1,num2):
     """
     Merhaba şuan bu fonkisyon için help metodunu deneyecem
     """
     if num1>num2:
          return f"{num1} büyüktür {num2}'den"
     elif num1<num2:
          return f"{num2} büyüktür {num1}'den"
     else :
          return "sayılar birbirine eşşitir"
     
num1=int(input("sayi1 "))
num2=int(input("sayi2 "))
print(get_greater_num(num1,num2))
help(get_greater_num) 