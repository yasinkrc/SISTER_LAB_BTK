""" 
Problem: Okul Not Kaydı

Bir okulun öğrenci not kayıtlarını içeren bir dosya yönetim sistemi oluşturmanız isteniyor. Öğrencilerin adı, soyadı ve matematik dersinden aldıkları not bilgileri kaydedilmelidir. Aşağıdaki işlemleri gerçekleştirecek bir program yazmanız gerekmektedir:

Program, kullanıcıdan öğrenci adını, soyadını ve matematik notunu almalıdır.
Kullanıcıdan alınan bu bilgiler, "notlar.txt" adlı bir dosyaya eklenmelidir. Her öğrenci bilgisi ayrı bir satırda saklanmalı ve öğrenci bilgileri arasında ":" karakteri ile ayrılmalıdır.
Örneğin: "Ali:Yılmaz:85"
Kullanıcı "q" tuşuna basana kadar not kaydı işlemine devam edebilmelidir.
Program sonlandığında, "notlar.txt" dosyasında kaydedilen tüm öğrenci bilgileri ekrana yazdırılmalıdır.
Not: Program her çalıştığında mevcut "notlar.txt" dosyasını kontrol etmeli ve eğer dosya yoksa otomatik olarak oluşturmalıdır.

Bu problemi çözmek için, Python'da dosya okuma ve yazma işlemlerini kullanmanız gerekmektedir. Dosya yönetimi konusundaki bilgilerinizi kullanarak bu problemi çözebilirsiniz. Başarılar!
"""



# class NotKaydi:
#     def __init__(self, dosya_adi):
#         self.dosya_adi = dosya_adi

#     def kaydet(self, ogrenci_ad, ogrenci_soyad, not_degeri):
#         with open(self.dosya_adi, "a") as dosya:
#             dosya.write(f"{ogrenci_ad}:{ogrenci_soyad}:{not_degeri}\n")

#     def oku(self):
#         with open(self.dosya_adi, "r") as dosya:
#             for satir in dosya:
#                 ogrenci_bilgisi = satir.strip().split(":")
#                 ogrenci_ad = ogrenci_bilgisi[0]
#                 ogrenci_soyad = ogrenci_bilgisi[1]
#                 not_degeri = ogrenci_bilgisi[2]
#                 print(f"Öğrenci: {ogrenci_ad} {ogrenci_soyad}, Matematik Notu: {not_degeri}")


# not_kaydi = NotKaydi("notlar.txt")

# while True:
#     ogrenci_ad = input("Öğrenci adını girin (q ile çıkış): ")
#     if ogrenci_ad == "q":
#         break

#     ogrenci_soyad = input("Öğrenci soyadını girin: ")
#     not_degeri = input("Matematik notunu girin: ")

#     not_kaydi.kaydet(ogrenci_ad, ogrenci_soyad, not_degeri)

# print("Kayıtlar:")
# not_kaydi.oku()
""" 
Problem: Film İnceleme

Bir film inceleme platformunda kullanıcıların film puanlarını kaydeden bir program yazmanız isteniyor. Kullanıcıdan film adı ve puanı alarak bu bilgileri bir dosyaya kaydedeceksiniz. Aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

Program, kullanıcıdan bir film adı ve puanı almalıdır.
Kullanıcıdan alınan bu bilgiler, "incelemeler.txt" adlı bir dosyaya eklenmelidir. Her film incelemesi ayrı bir satırda saklanmalı ve film adı ile puanı arasında ":" karakteri ile ayrılmalıdır.
Örneğin: "The Shawshank Redemption:9.2"
Kullanıcı "q" tuşuna basana kadar film inceleme işlemine devam edebilmelidir.
Program sonlandığında, ""incelemeler.txt"" dosyasında kaydedilen tüm film incelemeleri ekrana yazdırılmalıdır.
Not: Program her çalıştığında mevcut "incelemeler.txt" dosyasını kontrol etmeli ve eğer dosya yoksa otomatik olarak oluşturmalıdır.

Bu problemi çözmek için, yukarıdaki örnekte olduğu gibi dosya işlemlerini kullanarak bir Python programı yazabilirsiniz. Başarılar!
"""
    


# class Film:
#     def __init__(self, filename):
#         self.filename = filename

#     def movie(self, movieName, movieNote):
#         with open(self.filename, "a", encoding="utf-8") as file:
#             file.write(f"{movieName}:{movieNote}\n")

#     def oku(self):
#         with open(self.filename, "r") as file:
#             for satir in file:
#                 print(satir,end="")

# film_nesne = Film("incelemeler.txt")

# while True:
#     movieName = input("Film ismi giriniz (q ile de çıkış): ")
#     if movieName == "q":
#         break
#     movieNote = input("Film puanı giriniz: ")

#     film_nesne.movie(movieName, movieNote)

# film_nesne.oku()

""" 
Problem: Sözcük Frekansı

Bir metin dosyasındaki sözcükleri okuyan ve her bir sözcüğün kaç kez tekrarlandığını hesaplayan bir Python programı yazmanız isteniyor. Aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

Program kullanıcıdan bir metin dosyasının adını almalıdır.
Program, belirtilen dosyayı açmalı ve içindeki sözcükleri okumalıdır.
Okunan her sözcüğün frekansını hesaplayarak bir sözlükte saklamalıdır. Sözlükte, her bir sözcük anahtar ve frekansı değer olarak temsil edilmelidir.
Sözcük frekanslarına göre sıralanmış bir çıktı oluşturulmalıdır. Çıktıda, her bir sözcük ve frekansı ayrı bir satırda yer almalıdır.
Program sonlandığında, en yüksek frekansa sahip olan sözcüğü ve frekansını ekrana yazdırmalıdır.
Not: Metin dosyası içerisindeki her bir sözcük boşluk veya noktalama işaretleriyle ayrılmış kabul edilmelidir. Büyük-küçük harf duyarlılığı olmadan, yani "kelime" ile "Kelime" aynı sözcük olarak kabul edilmelidir.

Bu problemi çözmek için, dosya işlemleri ve sözlük kullanımını içeren bir Python programı yazabilirsiniz. Başarılar!
"""

# class WordFrequency:
#     def __init__(self, filename):
#         self.filename = filename

#     def calculate_frequency(self):
#         word_frequency = {}
#         with open(self.filename, "r" ,encoding="utf-8") as file:
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     word = word.lower()  # Küçük harfe dönüştürme
#                     if word in word_frequency:
#                         word_frequency[word] += 1
#                     else:
#                         word_frequency[word] = 1
#         return word_frequency

# file_name = "incelemeler.txt"
# word_counter = WordFrequency(file_name)
# frequency = word_counter.calculate_frequency()
# print(frequency)

""" 
Problem: İki Dosyanın İçeriğini Karşılaştırma

Bir metin dosyasının içeriğini diğer bir metin dosyasıyla karşılaştıran bir program yazmanız isteniyor. Programın aşağıdaki işlemleri gerçekleştirmesi gerekmektedir:

Kullanıcıdan iki metin dosyasının adını alın. Dosya adları geçerli dosyalara karşılık gelene kadar kullanıcıdan tekrar tekrar giriş yapılmalıdır.
Program, kullanıcının girdiği her iki dosyayı da açmalı ve dosya içeriğini okumalıdır.
Okunan dosya içerikleri karşılaştırılmalı ve herhangi bir farklılık varsa bu farklılık belirtilmelidir.
Farklılık olmadığı durumda, kullanıcıya "Dosyalar aynı" şeklinde bir mesaj gösterilmelidir.
Bu problemi çözmek için, yukarıdaki gereksinimleri karşılayan bir Python programı yazabilirsiniz. Programın, dosyaları satır satır karşılaştırması ve farklılık olduğu durumlarda bunu belirtmesi gerekmektedir.

Dosya 1: metin1.txt
Dosya 2: metin2.txt

Dosyalar farklı.


Dosya 1: metin1.txt
Dosya 2: metin2.txt

Dosyalar aynı.

"""


# class comparison :

#     def __init__(self ,filename1 ,filename2):
#         self.filename1=filename1

        
#         self.filename2=filename2
    
#     def two_file_comparison(self):
#         with open(self.filename1 ,"r",encoding="utf-8") as file1 :
#             with open(self.filename2,"r",encoding="utf-8") as file2 :
#                         if file1.read()==file2.read() :
#                             print("Dosyalar aynı.")
#                         else :
#                             print("Dosyalar farklı.")


# comparison1=comparison("incelemeler.txt","newfile.txt")
# comparison1.two_file_comparison()

""" 
Problem: Bir metin dosyası içindeki her bir kelimenin sayısını hesaplayan bir Python programı yazmanız gerekiyor. Program, kullanıcıdan bir dosya adı alacak, dosyayı açacak, her bir kelimenin sayısını hesaplayacak ve sonuçları ekrana yazdıracak. Program dosyayı okuduğunda, dosyayı hızlı bir şekilde kapatmalı.

Bu problemde, dosya açma, okuma, kelime sayısını hesaplama ve dosya kapatma becerilerinizi kullanmanız gerekecektir. İşte problemi çözmek için temel bir algoritma:

Kullanıcıdan bir dosya adı alın.
Dosyayı açın (open() işlevini kullanarak).
Dosyayı okuyun (read() işlevini kullanarak) ve içeriği bir dize değişkenine atayın.
Dosyayı kapatın (close() işlevini kullanarak).
Dizeyi kelimelere ayırın (split() işlevini kullanarak).
Bir kelime sayacı oluşturun ve her bir kelimeyi sayın.
Sonuçları ekrana yazdırın.
İşte bu adımları kullanarak bir Python programı oluşturabilirsiniz. Bu program, dosyayı açma, okuma ve kapatma işlemlerini doğru bir şekilde gerçekleştirir ve her bir kelimenin sayısını doğru bir şekilde hesaplar.

"""


# class repeat :

#     def __init__(self,filename):
#         self.filename=filename
    
#     def solve(self):

#         tekrarlama={}

#         with open(f"{self.filename}" , "r" ,encoding="utf-8") as file :

#             for satir in file :
#                 words=satir.split()

#                 for word in words :

#                     word=word.lower()

#                     if word in tekrarlama :

#                         tekrarlama[word]+=1
#                     else  :
#                           tekrarlama[word]=1
#         return tekrarlama


 

# objectrepeat=repeat("incelemeler.txt")
# print(objectrepeat.solve())


""" 

Problem: Bir metin dosyasındaki satırları tersine çeviren bir Python programı yazmanız gerekiyor. Program, kullanıcıdan bir dosya adı alacak, dosyayı açacak, her bir satırı tersine çevirecek ve tersine çevrilmiş satırları yeni bir dosyaya yazacak. Program dosyaları okuduğunda ve yazdığında, dosyaları hızlı bir şekilde açmalı ve kapatmalı.

Bu problemde, dosya açma, okuma, satır işleme ve dosya yazma becerilerinizi kullanmanız gerekecektir. İşte problemi çözmek için bir adım adım plan:

Kullanıcıdan bir giriş dosyası adı ve bir çıkış dosyası adı alın.
Giriş dosyasını açın (open() işlevini kullanarak) ve içeriği satır satır okuyun.
Her bir satırı tersine çevirin.
Çıkış dosyasını açın (open() işlevini kullanarak).
Tersine çevrilmiş satırları çıkış dosyasına yazın (write() işlevini kullanarak).
Giriş dosyasını kapatın.
Çıkış dosyasını kapatın.
İşte bu adımları kullanarak bir Python programı oluşturabilirsiniz. Program, giriş dosyasını açma, okuma ve kapatma işlemlerini doğru bir şekilde gerçekleştirirken, çıkış dosyasını açma ve yazma işlemlerini de doğru bir şekilde yapacaktır. Bu şekilde, metin dosyasındaki satırları tersine çevirebilir ve çıktıyı yeni bir dosyaya yazabilirsiniz.
"""


# class transfer :

#     def __init__(self,filename1 ,filename2):
#         self.filename1=filename1
#         self.filename2=filename2
    

#     def aktarma(self):

#         with open(self.filename1,"r",encoding="utf-8") as file1 :

#             with open(self.filename2 ,"w" ,encoding="utf-8") as file2 :

#                 for line in file1 :
                    
#                     line=line[::-1]

#                     file2.write(f"{line} \n")
            

#                 with open(self.filename2 ,"r" ,encoding="utf-8") as f :
                    
#                     print(f.read)
   

# objecttransfer=transfer("incelemeler.txt","newfile.txt")

# objecttransfer.aktarma()


""" 
Problem: Bir metin dosyasında farklı konulara ait bilgiler bulunmaktadır. Dosyayı açan ve her bir konuyu ayrı dosyalara bölen bir Python programı yazmanız isteniyor. Program, kullanıcıdan bir giriş dosyası adı ve bir çıkış dizini adı alacak, giriş dosyasını açacak, konulara göre dosyalar oluşturacak ve her bir konuyu ilgili dosyaya yazacak. Program dosyaları okuduğunda ve yazdığında, dosyaları hızlı bir şekilde açmalı ve kapatmalı.

Bu problemde, dosya açma, okuma, yazma, dizin oluşturma ve dosya kapatma becerilerinizi kullanmanız gerekecektir. İşte problemi çözmek için bir adım adım plan:

Kullanıcıdan bir giriş dosyası adı ve bir çıkış dizini adı alın.
Giriş dosyasını açın (open() işlevini kullanarak) ve içeriği satır satır okuyun.
Her satırı işleyerek konu bilgisini bulun.
Eğer konu daha önce işlenmemişse, ilgili dosyayı çıkış dizininde oluşturun.
Konuya ait dosyayı açın (open() işlevini kullanarak).
Satırı ilgili dosyaya yazın (write() işlevini kullanarak).
Giriş dosyasını kapatın.
Konu dosyalarını kapatın.
Bu adımları takip ederek, metin dosyasındaki farklı konuları ayrı dosyalara bölen bir Python programı oluşturabilirsiniz. Bu şekilde, her bir konu için ayrı dosyalar oluşturabilir ve ilgili bilgileri doğru dosyalara yazabilirsiniz.

"""

# import os

# class KonuAyirici:

#     def __init__(self, girdi_dosyasi, cikti_dizini):
#         self.girdi_dosyasi = girdi_dosyasi
#         self.cikti_dizini = cikti_dizini

#     def konulara_ayir(self):
#         konular = {}

#         with open(self.girdi_dosyasi, "r", encoding="utf-8") as girdi_dosya:
#             for satir in girdi_dosya:
#                 if satir.strip():  # Boş olmayan satırları işle
#                     konu = satir.strip().split(":")[0]  # Satırın başındaki konu bilgisini al
#                     icerik = satir.strip().split(":")[1]  # Satırın geri kalanını içerik olarak al

#                     if konu in konular:
#                         konular[konu].append(icerik)
#                     else:
#                         konular[konu] = [icerik]

#         # Her bir konuya ait dosyaları oluştur ve içerikleri yaz
#         for konu, icerikler in konular.items():
#             konu_dosyasi = os.path.join(self.cikti_dizini, f"{konu}.txt")

#             with open(konu_dosyasi, "w", encoding="utf-8") as cikti_dosya:
#                 for icerik in icerikler:
#                     cikti_dosya.write(f"{icerik}\n")

#         print("Konulara ayrılan dosyalar oluşturuldu.")

# # Kullanım örneği
# ayirici = KonuAyirici("girdi.txt", "cikti_dizin")
# ayirici.konulara_ayir()



