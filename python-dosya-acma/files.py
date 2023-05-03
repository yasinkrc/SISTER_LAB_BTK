#Dosyayı oluşturmak için open() fonkiyonu kullanılılır 
#Kullanımı : open (dosya_adi , dosya erişme modu )
#Dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir


# "W" : (Write) yazma modu  :  Dosyayı konumda oluşturur 

# open("newfile.txt","r")  ==> hata veriri çünkü "r" (read ) okuma yapacak ama dosya yok 

# file =open("newfile.txt","w")

# print(file)

# file.close()

# file=open("C:/Users/yasin/OneDrive/Masaüstü/SISTER_LAB_BTK/newfile.txt","w")
# file.close()





# file =open("newfile.txt","w",encoding="utf-8")
# file.write("Sadık Turan \n ") #Sad�k Turan böyle bir olayla karşılarsan encodig="uft-8" yaz
# file.write("hello word ")
# file.close()



# "a" => (Append) ekleme . Dosya konumunda yoksa  oluşturu .
# file =open("newfile.txt","a",encoding="utf-8") 
# file.write(" \nsadik turan  ")
# file.close()

# "x" => (Create) oluşturma  . Dosya zaten varsa hata verir .

file =open("newfile2.txt","x",encoding="utf-8") 



 