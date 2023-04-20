#1- Girilen bir sayının 0-100 arasında olup oladdığını kontrol ediniz 

# sayı=int(input("Sayıyı giriniz : "))

# if (0<sayı<100):
#     print(f"Evet {sayı}'sayısı  bu aralıkta")
# else :
#     print(f"Hayır {sayı}'sı bu aralıkta değil ")




#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# sayı=int(input("Sayıyı giriniz : "))

# if (0<sayı):
#     print(f"Evet {sayı}'sayısı  pozitif ")
# elif (sayı<0):
#     print(f"Hayır {sayı}'sı negatif ")
# else :
#     print("Sayımız O dır ")

#3- E mail ve parola bilgileri ile giriş kontrolu yapınız

# email="email@sadikturan.com"
# parola="abc123"

# emailK=input("E-mailinizi giriniz.")
# parolaK=input("Parolanızı Giriniz ")

# if(email==emailK) :
#     if(parola==parolaK):
#         print("Giriş başarılı")
#     else :
#         print("e mail doğru ama parola yanlış lütfen tekrar deneyiniz .")
# else :
#     print("giriş bilgilerin yanlış lütfen tekrar giriniz ")
#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

# sayı1=int(input("1.Sayıyı giriniz : "))
# sayı2=int(input("2.Sayıyı giriniz : "))
# sayı3=int(input("3.Sayıyı giriniz : "))

# if(sayı1>sayı2) :
#     if(sayı1>sayı3):
#         print(f"en buyuk sayi {sayı1} dir")
#     else:
#         print(f"en buyuk sayı {sayı3} dur ")
#         print(f"ortanca sayı {sayı1} dur ")
#         print(f"en kucuk sayı {sayı2} dur ")
# elif (sayı2>sayı1)  :
#     if(sayı2>sayı3):
#         print(f"en buyuk sayi {sayı2} dir")
#     else:
#         print(f"en buyuk sayı {sayı3} dur ")
#         print(f"ortanca sayı {sayı2} dur ")
#         print(f"en kucuk sayı {sayı1} dur ")
# elif (sayı3>sayı1)  :
#     if(sayı3>sayı2):
#         print(f"en buyuk sayi {sayı3} dir")
#     else:
#         print(f"en buyuk sayı {sayı2} dur ")
#         print(f"ortanca sayı {sayı3} dur ")
#         print(f"en kucuk sayı {sayı1} dur ")
# else :
#     print(f"tüm sayılar birbirine eşir {sayı1}{sayı2}{sayı3}")
#5- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama  hesaplayınız
""" Eğer ortalama 50 ve  üstündeyse geçti değilse kaldı yazdırın """ 
""" a-)Ortalama 50 olsa bile final notu en az 50 olmalıdır       """
""" b-)Finalden 70 alındığında ortalamanın bir önemi olmasın     """

# vize1=int(input("vize1 notunu gir ."))
# vize2=int(input("vize2 notunu gir ."))
# final=int(input("final notunu gir ."))

# vizeT=(vize1+vize2)*0.6
# ort=vizeT+final*0.4

# if (ort>=50):
#     if(final>=50) :
#         print("tebrikler başarıyla geçtiniz")
#     else :
#         print("ne yaziki final notunuz geçmenize müsade etmiyor")
# elif(ort<50) and (final>=70):
#     print("tebrikler ortalama düşük ama siz yine de final notunuz sayesinde  geçtiniz")
# else :
#     print("üzgünüm kaldınız")



#6- Kişinin ad , kilo ve boy biilgileriini alıp kilo indekslerini hesaplayınız .
"""   
Formül : (kilo / boy uzunluğunun karesi)
 Aşağıdaki tabloya göre kişi hangi gruba girmektedir 
 0-18.4 --> ZAYIF
  18.05-24.9 -->NORMAL
    25.0-29.9 --> FAZLA KİLOLU
      30.-34.9 --> ŞİŞMAN (OBEZ)
     
"""

name=input("İsim : ")
kilo =int(input("kilo : "))
boy=float(input("boy :"))

hg=(kilo / boy**2)

if ( 0<hg<18.4) :
    print(f"{name} işte indeksin {hg} bu sonuçla sonucun zayıf ")
elif(18.05<hg<24.9):
    print(f"{name} işte indeksin {hg} bu sonuçla sonucun normal ")
elif(25.0<hg<29.9):
    print(f"{name} işte indeksin {hg} bu sonuçla sonucun fazla kilolu ")
elif( 30.0 <hg<34.9):
    print(f"{name} işte indeksin {hg} bu sonuçla sonucun obez ")
else :
    print("sen bitmişsin be kral ")
