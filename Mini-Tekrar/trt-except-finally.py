# print(1)
# print(2)
# print(x)
# print(3)
# print(4)
# print(1)
# print(2)
# try :
#  print(x)
# except :
#  print("x değişkeni tanımlanmamış")

# print(3)
# print(4)


# num1=10
# try:
#  num2=int(input("Bölen sayiyi giriniz "))
#  result=num1/num2
#  dosya=open("olmayandosya.txt")
# except ZeroDivisionError:
#  print("o değeri girilemez")
# except ValueError:
#  print(" string  değeri girilemez")
# except :
#  print("Tanımlanamayan hata ")

# # print(result)


# num1=10
# try:
#  num2=int(input("Bölen sayiyi giriniz "))
#  result=num1/num2
# #  dosya=open("olmayandosya.txt")
#  print(result)
# except ZeroDivisionError:
#  print("o değeri girilemez")
# except ValueError:
#  print(" string  değeri girilemez")
# except : #hatavarsa
#  print("Tanımlanamayan hata ")
# else :#hata yoksa 
#  print("Hiçbir hata yok ")
# finally :
#  print("her türlü çaloşın")

# num1 =0

# if num1 ==0 :
#     raise Exception ("Değer sıfır olamaz")

# num1 =0

# if num1 ==0 :
#     raise ZeroDivisionError ("Değer sıfır olamaz")

# num1 =0

# if num1 ==0 :
#     raise ValueError("Değer string olamaz")

num1="ASD"

if not type(num1) is int :
    raise ValueError("Lütfen sayısal bir değer girin")