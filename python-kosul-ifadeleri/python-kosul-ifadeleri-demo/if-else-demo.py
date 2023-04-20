""" 1- Kullanıcıdan isim , yas ve eğitim bilgilerini isteyip ehliyet alabilme 
    durumunu kontrol ediniz . Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da
    üniverisite olmalıdır .  
"""
# isim=input("isim :")
# yas=int(input("yas : "))
# egitim=input("eğitim :")

# if (yas>=18 and egitim=="lise"or egitim=="üniversite"):
#     print(f"{isim} ehliyet alma hakkınız var ")
# else:
#      print(f"{isim} ehliyet alma hakkınız yok ")

# if (yas>=18):
#     if(egitim=="lise"or egitim=="üniversite"):
#         print("ehliyet alabilirsiniz")
#     else:
#         print("ehliyet alamazsınız eğitim duruumunuz münasip değil")
# else :
#     print("ehliyet alamazsınız yaşınız tutmuyor .")    


""" 2-- Bir öğrencinin 2 yazılı bir sözlü notunu alığ hesaplanan ortalamaya göre 
    not aralığına karşılık gelen not bilgisini yazdırınız ?

    0-24   --0
    25-44  --1
    45-54  --2 
    55-69  --3
    70-84  --4
    85-100 --5
"""
# vize1 =int(input("vize1 : ") )
# vize2 =int(input("vize2 : "))
# final =int(input("final : "))

# o=(vize1+vize2+final)/3


# if  0<o<24 :
#     print("0",o)
# elif 25<o<44 :
#     print("1",o)
# elif 45<o<54 :
#     print("2",o)
# elif 55<o<69 :
#     print("3",o)
# elif 70<o<84 :
#     print("4",o)
# elif 85<o<100 :
#     print("5",o)

""" 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınız .
    1.Bakım -- 1.yıl
    2.Bakım -- 2.yıl
    3.Bakım --3.yıl

    ** Süre hesabını alınan gün , ay , yıl bilgisine göre gün bazlı hesaplayınnız 
    *** datetime modülünü kullanmanız gerekiyor 
    örn: şimdi -(2018/8/1)--gün 

"""
import datetime
tarih=(input("aracınız hangi tarihte trafike çıktı -- (2019/8/9) : "))
tarih=tarih.split("/")


# print(tarih[0])
# print(tarih[1])
# print(tarih[2])
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi =datetime.datetime.now()
fark=simdi-trafigeCikis
print(fark.days)
days=fark.days
if days<=365 :
     print("1.servis aralığı")
elif days >365 and days<=365*2:
    print("2.servis aralığı")
elif days >365*2 and days<=365*3:
    print("3.servis aralığı")
else :
    print("hatalı süre ")