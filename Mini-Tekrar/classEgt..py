class Ogrenci() :
    """ __init__  fonksiyonu pythonda ilk çalışan fonksiyondur """
    def __init__(self,gelenAd , gelenVize1 ,gelenVize2 ,gelenFinal):
          self.ad =gelenAd
          self.vize1=gelenVize1
          self.vize2=gelenVize2
          self.final=gelenFinal
          print(f"{gelenAd} öğrencisi oluşturuldu ")
          

    def not_hesaplama(self):
          return (self.vize1*(30/100)+(self.vize2*(30/100)+(self.final+(40/100))))

    def bigileiYazdir(self):
         not_hesaplama2 =(self.vize1*(30/100)+(self.vize2*(30/100)+(self.final+(40/100))))
         print(f"{self.ad} isimli öğrencinin 1. vizesi : {self.vize1} , 2.vizesi : {self.vize2} ,final notusu :{self.final} bu öğrencinin not ortalaması ise {Ogrenci.not_hesaplama(self)} ")
     



""" Constructor kullandık bu sefer """

ogr1 =Ogrenci("Burak ",20,40,50)
# print(ogr1.ad)

ogr2 =Ogrenci("Ahmet ",30,50,30)
# print(ogr2.ad)

ogr3 =Ogrenci("Sıla ",66,55,77)

print(ogr1.not_hesaplama())
print(ogr1.bigileiYazdir())

print(ogr2.not_hesaplama())
print(ogr2.bigileiYazdir())
# ogr1=Ogrenci()
# print(ogr1.ad)
# print(ogr1.vize1)

# """ TEKRAR BURAK GELDİ BİR ŞEYLER YAPMALIYIZ """
# ogr2=Ogrenci()
# print(ogr2.ad)
# print(ogr2.vize1)

