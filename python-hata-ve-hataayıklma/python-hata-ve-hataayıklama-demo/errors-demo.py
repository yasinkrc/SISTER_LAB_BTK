liste =["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz .
""" Benim  çözümüm """
# try :
#     for i in liste :
#         print(int(liste[i]))
# except :
#     print("haricindeki sayılar olmuyor idare et ")
#     print(int(liste[i]))
""" Cevap anahtarı """
# for x in liste :

#     try :
#         result=int(x)
#         print(result)
#     except ValueError:
#         continue 

# 2:Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz 
# aksi halde hata mesajı yazınız
""" Cevap anahtarı """

# while True :
#    sayi=input("sayi")
#    if sayi=="q":
#      break
   
#    try :
#       result=float(sayi)
#       print(f"girdiğiniz sayi {sayi}")
#    except ValueError:
#       print("geçersiz sayı")
#       continue

# 3:Girilen parola içindeki türkçe karekter hatası veriniz
""" Cevap anahtarı """
# def check_password(parola):
#     turkce_karakterler ="şçğüöı"
#     for i in paralo :
#             if i in turkce_karakterler:
#                 raise TypeError("Parola türkçe karekter içeremez")
#             else :
#                 pass
            
#     print("geçerli parola")

# paralo=input("parola: ")

# try:
#      check_password(paralo)

# except TypeError  as err:
#      print(err)

 


# 4: faktöriyel fonksiiyonu oluşturup fonksiyona gelen değer için hata mesajları verin
""" Cevap anahtarı """ 

def faktoriyel(x):

    x =int(x)

    if x <0 :
        raise ValueError("negatif değer")
    
    result=1

    for i in range(1,x+1):
        result*=i
    return result

for  x in [5,10,20,-3,"10a"]:
    try :
        y=faktoriyel(x)

    except ValueError as err  :
        print(err)
        continue
print(y)