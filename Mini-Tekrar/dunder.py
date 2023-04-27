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
     

    def __repr__(self) :
         return "selam kelebek"
    def __add__(self,other):
         return "Merhaba"+other

""" Constructor kullandık bu sefer """

ogr1 =Ogrenci("Burak ",20,40,50)
# print(ogr1.ad)
print(ogr1)
print(ogr1,"naber")
print(dir(ogr1))