#1-"Bmw , Mercedes , Opel , Mazda" elemanlarına sahip bir liste oluşturunuz 
arabalar=["Bmw","Mercedes","Opel","Mazda"]
#2-Liste kaç elemanlıdır ?
result =len(arabalar)
#3-Listenin ilk ve son elemanı nedir ?
result=arabalar[0]

result=arabalar[3]

result=arabalar[-1]

#4-Mazda değerini Toyata ile değiştirin
arabalar[-1]="Toyata"
result=arabalar
#5-Mercedes listenin bir elemanı mıdır ?
result="Mercedes" in arabalar
#6-Listenin -2 indeksindeki değer nedir 
result=arabalar[-2]
#7-Listenin ilk 3 elemanını alın 
result=arabalar[:3]
#8-Listenin son 2 elemanı yerine "Toyata" ve "Renault" değerlerini ekleyin
arabalar[-2:]="Toyata","Renault"
result=arabalar
#9-Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
newlist=["Audi","Nissan"]

result=arabalar+newlist
#10-Listenin son elemanını silin
del arabalar[-1]
result=arabalar
#11-Liste elemanlarını tersten yazdırın 
result=arabalar[::-1]
#12-Aşağıdaki verileri bir liste içinde saklayınız .
      
     # stundentA: Yiğit Bilgi  2010 ,(70,60,70)
     # stundentB: Sena Turan   1999 ,(80,80,70)
     # stundentC: Ahmet Turan  2010 ,(70,60,70)
stundentA=["Yiğit","Bilgi" ,2010,[70,60,70]]
stundentB=["Sena" ,"Turan" ,1999,[80,80,70]]
stundentC=["Ahmet","Turan" ,2010,[70,60,70]]

ogrenciller =[stundentA ,stundentB ,stundentC]
result=stundentA[0]
result=stundentB[1]
result=stundentC[3][2]
ortalama=(stundentA[3][0]+stundentA[3][1]+stundentA[3][2])/3
result=f"{stundentA[0]} {stundentA[1]} {2019-stundentA[2]} yaşında ve not ortalaması {ortalama:1.15}"
print(ogrenciller)
print(result)