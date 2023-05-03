
# try :
#     file=open("newfile.txt","r")
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally :
#     print("dosya kapandı")
#     file.close()

file =open("newfile.txt","r",encoding="utf-8")

#for döngüü 

# for i in file :
#     print(i,end="")
# file.close()

#************************* read() fonksiyonu


# content=file.read()

# print("içerik1")
# print(content)

# file =open("newfile.txt","r",encoding="utf-8")
# content2=file.read()
# print("içerik2")
# print(content2)

# content=file.read(5)
# print(content)


#************************* readline() fonksiyonu
#readline( her fonksiyonda bir satır okur )


# content=file.readline()
# print(content)
# content=file.readline()
# print(content)

# print(file.readline(),end="")

# print(file.readline(),end="")

# print(file.readline(),end="")

# print(file.readline(),end="")

# print(file.readline(),end="")

#************************* readlines() fonksiyonu
liste =file.readlines()
print(liste)
print(liste[0],end="")
print(liste[1],end="")
print(liste[2],end="")


file.close()