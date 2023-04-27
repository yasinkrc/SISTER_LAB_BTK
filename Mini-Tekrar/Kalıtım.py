class Insan():

    def __init__(self,gelenAd ,gelenSoyad) :
        self.ad=gelenAd
        self.soyad=gelenSoyad

    def bilgileri_Yazdir(self) :
        return f"""
        -------- Kişi Bilgileri -------
        Ad :{self.ad}
        Soyad :{self.soyad}
        """
class Ogrenci(Insan):
    def __init__(self , gelenAd ,gelenSoyad, gelenNot) :
        Insan.__init__(self,gelenAd,gelenSoyad)
        self.notu=gelenNot

    def bilgileri_Yazdir(self) :
        return Insan.bilgileri_Yazdir(self)+f"""not :{self.notu}
        """
       
class Ogretmen(Insan):
    def __init__(self , gelenAd ,gelenSoyad, gelenmaas) :
        Insan.__init__(self,gelenAd,gelenSoyad)
        self.maas=gelenmaas
    def bilgileri_Yazdir(self) :
        return Insan.bilgileri_Yazdir(self)+f"""not :{self.maas}
        """
       
ogretmen =Ogretmen("Ahmet","yaşar",5000)
print(ogretmen.bilgileri_Yazdir())
insan1=Insan("Yasin","Karaca")
print(insan1.bilgileri_Yazdir())

ogrenci1=Ogrenci("Yazgülü","Karaca",52)
print(ogrenci1.bilgileri_Yazdir())