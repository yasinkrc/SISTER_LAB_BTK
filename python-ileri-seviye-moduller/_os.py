import os 
import datetime
from os import stat


result=dir(os)
result=os.name

""" Klasör konum değiştirme """
# os.chdir("C:\\")
# os.chdir("..")
# os.chdir("..")
# os.chdir("..\..")

"""Klasör oluşturma"""
# os.mkdir("newdirectory")
# os.rename("newdirectory","yeni klasör ")

# os.makedirs("newdirectory/yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeni klasör/yeniklasör")

""" Etkin dizi öğrenme """
# result=os.getcwd()

""" Listeleme"""

# result=os.listdir()
# result=os.listdir("C:\\")

# for dosya in os.listdir():
#     if dosya.endswith('py'):
#         print(dosya)
#     else :
#         print("değil",dosya)



 # Bilgi almak istediğiniz dosyanın adını belirtin

# result = os.stat('date.py')

""" Dosya hakkındaki bilgileri alabilirsiniz"""
# print("Dosya Boyutu:", result.st_size, "byte")
# print("Oluşturma Zamanı:", result.st_ctime)
# print("Son Erişim Zamanı:", result.st_atime)
# print("Son Değiştirme Zamanı:", result.st_mtime)


# os.system("notepad.exe")


""" Path Sınıfı """

""" 
path sınıfı daha çok uzantılarla ilgileniyor 
bunların uzantılarını değiştirme gibi 
mesela bir taneresim var ve upload edeceksiniz aynı isimde ise ismini değiştirmek isterseniz
bunu kullanabillirsiniz 
"""

result=os.path.abspath("_os.py")
result=os.path.dirname("c:/Users/yasin/OneDrive/Masaüstü/SISTER_LAB_BTK/python-ileri-seviye-moduller/_os.py")
# result=os.pardir.dirname(os.path.abspath("_os.py"))
result=os.path.exists("image.png")
# result=os.isdir("c:/Users/yasin/OneDrive/Masaüstü/SISTER_LAB_BTK/python-ileri-seviye-moduller/_os.py")
result=os.path.join("C:\\","deneme")
result=os.path.join("C:\\","deneme","deneme_1")
result=os.path.split("C:\\deneme")
result=os.path.splitext("_os.py")
# result=result[0]
result=[1]

print(result)