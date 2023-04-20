"""" 

1-100 arasında rastegele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın 
** "random mödülü" için "python random " şeklinde araştırma yapın
** 100 üzerinden puanlama yapın . Her soru 20 puan 
**  Hak bilgisi kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın


"""
import random 

sayi=random.randint(1,100)

can =int(input("kaç hak almakk istiyorsunuz "))
hak=can
sayac=0
print("tahmin: ",sayi)

while(hak>0) :
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin :"))

    if tahmin==sayi :
        print(f"tebrikler {sayac}. defada bildiniz. Toplam puanınız : {100-(100/can)*(sayac-1)}")
        break
    elif sayi>tahmin:
        print("Yukarı")
    else :
        print("aşağı")
    if hak==0 :
        print(f" hakkınız bitti {sayi}")
