""" 
Soru : Girilen bir sayının asal olup olmadığını bulun .

 ** asal Sayı kendisi hariç tam böleni olmayan sayılara denir 

"""


sayi=int(input("Sayınızı giriniz"))

degisken=sayi
asalmı=True

if sayi<2 :
    print("sayı asal değildir ")

for i in range(2,sayi):

 if sayi%i==0 :
    asalmı=False
    break

print(f"{sayi} sayısı asal mi : {asalmı}")