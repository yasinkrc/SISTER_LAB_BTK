#1- Girilen bir sayının 0-100 arasında olup oladdığını kontrol ediniz 

# x=int(input("Sayı: "))

# result=(0<x<100)

# print(f"{x} sayısı o aralıkta mı : {result}")


#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# x=int(input("Sayı: "))

# result=(x>0)and(x%2==0)

# print(f"{x} sayısı pozitif çift sayı mı  : {result}")

#3- E mail ve parola bilgileri ile giriş kontrolu yapınız
# email="email@sadikturan.com"
# parola="abc123"

# emailK =input("kullanıcı e-mailini giriniz : ")
# parolaK =input("kullanıcı parolasını  giriniz  : ")

# emailK.strip()
# parolaK.strip()
# emailK.lower()
# parolaK.lower()


# emailKontrool=(email==emailK)
# parolaKontrol=(parola==parolaK)

# result=(emailKontrool and parolaKontrol)

# print(f"E mail : {emailKontrool } ve parola : {parolaKontrol} bilgileri ile giriş kontrolu yapma doğru mu : {result} ")





#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

# x,y,z=int(input("Sayi1 : ")) , int(input("Sayi2 : ")) ,int(input("Sayi3 : "))

# result=(x>y) and (x>z)
# print(f"x en büyük sayıdır : {result} ")
# result=(y>x) and (y>z)
# print(f"y en büyük sayıdır : {result}")
# result=(z>y) and (z>x)
# print(f"z en büyük sayıdır : {result} ")

#5- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama  hesaplayınız
""" Eğer ortalama 50 ve  üstündeyse geçti değilse kaldı yazdırın """ 
""" a-)Ortalama 50 olsa bile final notu en az 50 olmalıdır       """
""" b-)Finalden 70 alındığında ortalamanın bir önemi olmasın     """

# vize1,vize2,final=int(input("Vize1 : ")) , int(input("Vize2 : ")) ,int(input("Final : "))

# vizeK=(vize2+vize1)*0.6
# ortalama=vizeK+(final*0.4)

# result=ortalama>=50 and final>=50 
# print(f"Başarıyla geçti mi : {result}")

# result=final>=70 or ortalama>=50
# print(f"Başarıyla geçti mi : {result}")


#6- Kişinin ad , kilo ve boy biilgileriini alıp kilo indekslerini hesaplayınız .
"""   
Formül : (kilo / boy uzunluğunun karesi)
 Aşağıdaki tabloya göre kişi hangi gruba girmektedir 
 0-18.4 --> ZAYIF
  18.05-24.9 -->NORMAL
    25.0-29.9 --> FAZLA KİLOLU
      30.-34.9 --> ŞİŞMAN (OBEZ)
     
"""

isim =input("name:")
kilo=int(input("kilo"))
boy=float(input("height"))
hg=(kilo/boy**2)

zayif=(hg>=0) and (hg<=18.04)
normal=(hg>18.04) and (hg<=24.09)
şişman=(hg>24.09) and (hg<=29.09)
obez=(hg>29.09) and (hg<=34.09)

print(f"{isim} kilo indeksin :  {hg} ve kilo değerlendirmen  zayıf : {zayif}  ")
print(f"{isim} kilo indeksin :  {hg} ve kilo değerlendirmen  normal : {normal}  ")
print(f"{isim} kilo indeksin :  {hg} ve kilo değerlendirmen  şişman : {şişman}  ")
print(f"{isim} kilo indeksin :  {hg} ve kilo değerlendirmen  obez : {obez}  ")
