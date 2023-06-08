""" 
Problem: Bir JSON dosyasında depolanan bir kitap listesi var. 
Her kitap bir başlık, yazar ve yayın tarihi içeriyor.
Kullanıcıya, kitap başlığını girdikten sonra, 
programın bu kitabı bulup yazarını ve yayın tarihini ekrana yazdırmasını istiyoruz
"""
# import json

# class Book: 
#     def __init__(self, bookName, author, time):
#         self.bookName = bookName
#         self.author = author
#         self.time = time

# class BookRepository:
#     def yaz(self, user: Book):
#         data = {
#             "bookName": user.bookName,
#             "author": user.author,
#             "time": user.time
#         }

#         with open("users.json", "w", encoding="utf-8") as file:
#             json.dump(data, file)
#             file.write("\n")  # Her veriyi yeni bir satıra yazmak için

# nesneR = BookRepository()

# while True:
#     secim = input("1-ekle\n2-yazdır\n3-Çıkış\nSeçim: ")

#     if secim == '3':
#         break
#     else:
#         if secim == '1':
#             bookName = input("bookname: ")
#             author = input("author: ")
#             time = input("time: ")
#             nesne = Book(bookName, author, time)
#             nesneR.yaz(nesne)
#         elif secim == '2':
#             pass
#         else:
#             print("yanlış bir sonuç girdiniz")

# import datetime 
""" 

Kolay Seviye:
Soru: Bugün hangi gün olduğunu nasıl bulabilirim?

Orta Seviye:
Soru: İki tarih arasındaki gün sayısını hesaplamak için datetime modülünü nasıl
kullanabilirim?

Zor Seviye:
Soru: Kullanıcıdan bir doğum tarihi alarak, 
kaç yaşında olduğunu ve yaşının 10, 25 ve 50 yıllık dönüm noktalarındaki 
doğum günlerinin ne zaman olduğunu hesaplayan bir program nasıl yazabilirim?

+1 Seviye:
soru: Bir kullanıcıdan doğum tarihini (gün, ay, yıl) alan
 ve bu doğum tarihine göre kullanıcının kaç yaşında olduğunu hesaplayan bir
 Python programı yazmanız gerekiyor.
 datetime modülünü kullanarak kullanıcının yaşını hesaplayan bir fonksiyon oluşturun.

"""

# from datetime import datetime 

# simdi=datetime.now()

# gun_adi=simdi.strftime("%A")

# print(gun_adi)



# from datetime import datetime


# simdi=datetime.now()
# gecmis=datetime.fromtimestamp(0)


# fark=simdi-gecmis

# fark=fark.days

# print(fark)


# from datetime import datetime

# dogum_tarihi=datetime(2001,11,28,12,30,56)

# simdi=datetime.now()

# fark=simdi-dogum_tarihi
# fark=fark.days
# fark=fark/365

# print(f"{fark:2.1}")

# from datetime import datetime 

# dogum_tarihi=input("Merhaba lütfen doğum tarihinizi giriniz ? (gün, ay, yıl) ")

# dogum_tarihi_1 =datetime.strptime(dogum_tarihi,"%d %B %Y")

# simdi=datetime.now()

# fark=simdi-dogum_tarihi_1

# print(int(fark.days/365.0))


""" 
Soru: Bir kişi, bir dizi etkinlik için farklı tarihlerde ve saatlerde buluşmalara katılacak. 
Her buluşmanın başlangıç ve bitiş saatleri veriliyor. 
Kişi, tüm buluşmalara ne kadar süreyle katılacağını hesaplamak istiyor. 
Bu durumu timedelta kullanarak nasıl çözebiliriz?


"""
from datetime import datetime, timedelta

bulusmalar = [
    {
        'baslangic': datetime(2023, 6, 7, 14, 30),
        'bitis': datetime(2023, 6, 7, 16, 0)
    },
    {
        'baslangic': datetime(2023, 6, 8, 9, 30),
        'bitis': datetime(2023, 6, 8, 12, 0)
    },
    {
        'baslangic': datetime(2023, 6, 9, 10, 0),
        'bitis': datetime(2023, 6, 9, 11, 30)
    }
]

toplam_katilma_suresi = timedelta()

for bulusma in bulusmalar:
    baslangic = bulusma['baslangic']
    bitis = bulusma['bitis']
    sure = bitis - baslangic
    toplam_katilma_suresi += sure

print("Toplam katılma süresi:", toplam_katilma_suresi)

# from datetime import datetime, timedelta

# enter_time = datetime(2023, 6, 8, 12, 00, 00)
# end_time = enter_time + timedelta(hours=4)

# simdi = datetime.now()

# fark = end_time - simdi

# print(fark)

