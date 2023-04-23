# def sayHello(name=" user "):
#     print("Hello "+name)


# sayHello("Çınar")

# sayHello("Ada")

# sayHello()


def sayHello(name=" user "):
    return ("Hello "+name)


msg=sayHello("Çınar")

print(msg)



def total(num1 ,num2) :

    return num1+num2

result=total(1,2)
print(result)
result=total(3,2)
print(result)


def yasHesapla(dogumYili) :
   return 2019-dogumYili

ageÇınar =yasHesapla(2017)

ageAda =yasHesapla(2040)

ageSena =yasHesapla(5264)

print(ageÇınar,ageAda,ageSena)


def EmeklilikgeKacYilKaldi(dogumYili ,isim):
    """ 
    DOCSTRİNG : Doğum yılınıza göre emekliliğinize kaç yıl kaldı 
    INPUT : DOĞUM YILI
    OUTPUT : HESAPLANA YIL 
    """
    yas=yasHesapla(dogumYili)

    emeklilik=65-yas

    if emeklilik>0 :
      print(f"Emekliğinize {emeklilik} 'yıl kaldı")
    else :
       print("zaten emekli oldunuz ")

EmeklilikgeKacYilKaldi(1983 ,"Yasin")
EmeklilikgeKacYilKaldi(1950 ,"Yazgülü")
EmeklilikgeKacYilKaldi(1990 ,"Ahmet")

print(help(EmeklilikgeKacYilKaldi))