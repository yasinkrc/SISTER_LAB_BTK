""" 

1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız .

2-Öğrenci numarasanı kullanıcıdan alıp ilgili öğrenci bilgisini göterin

"""

ogrenci1no =int(input("öğrenci1 no gir"))
ogrenci2no =int(input("öğrenci2 no gir"))
ogrenci3no =int(input("öğrenci3 no gir"))

ad1=input("öğrenci1 isim gir")
ad2=input("öğrenci2 isim gir")
ad3=input("öğrenci3 isim gir")

soyad1=input("öğrenci1 soyad gir")
soyad2=input("öğrenci2 soyad gir")
soyad3=input("öğrenci3 soyad gir")

telefon1=input("öğrenci1 telefon gir")
telefon2=input("öğrenci2 telefon gir")
telefon3=input("öğrenci3 telefon gir")


ogrenciler={

  ogrenci1no :{
    'ad':ad1,
    'soyad':soyad1,
    'phone':telefon1
  },
  ogrenci2no:{
    'ad':ad2,
    'soyad':soyad2,
    'phone':telefon2
  },
  ogrenci3no : {
    'ad':ad3,
    'soyad':soyad3,
    'phone':telefon3
  }

}

print(ogrenciler)
print(ogrenciler[ogrenci1no])
print(ogrenciler[ogrenci2no])
print(ogrenciler[ogrenci3no])
print(ogrenciler[ogrenci1no]['ad'])
print(ogrenciler[ogrenci2no]['ad'])
print(ogrenciler[ogrenci3no]['ad'])

