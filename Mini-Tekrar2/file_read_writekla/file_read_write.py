import random
""" 
1-Dosya açma
2-İslemi yap
3-dosyayi kapat 
"""

""" İşlem modları 
****** W *******
"""
# benim_dosyam = open("blabla.txt", "w")
# benim_dosyam.write("Python dersi \n")
# benim_dosyam.close()


isimler = ["beyza","yazgülü","yasin","emin","merve","simge","metin","ahmet"]

numara=[random.randint(5000,9999) for i in range(len(isimler))]
   

# print(numara)

f=open("blabla.txt","w",encoding="utf-8") 

for i in range(0,len(isimler)):
    f.write(f" {str(numara[i])} : {isimler[i]} \n")

f.close()
