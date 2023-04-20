names =["Ali","Yağmur","Hakan","Deniz"]

years=[1998 ,2000,1998,1987]

# 1-"Cenk" ismini listenin sonuna ekleyiniz 
names.append("Cenk")
# 2-"Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
# 3-"Deniz" ismini listeden siliniz
#  names.remove("Deniz")
# 4-"Deniz" isminin indeksi nedir ?
print(names.index("Deniz"))
# 5-"Ali" listenin bir elemanımıdır ?
print("Ali" in names)
# 6-Liste elemanlarını ters çevirin .
names.reverse()
# 7-names  listesini alapahatk büyüklüğe göre sıralayınız.
names.sort()

# 8-years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
# 9-str ="Chevrolet ,Dacia" karekter dizisini listeye çeviriniz.
str ="Chevrolet,Dacia" 
str.split(",")
print(str)
# 10-years dizisinin en büyük ve en küçük elemanı nedir ?
print(max(years))
print(min(years))
# 11- years dizisinde kaç tane 1998 değeri vardir ?
print(years.count(1998))
# 12-years dizisinin tüm elemanlarını siliniz .
years.clear()
# 13-Kullanıcıdan alacağınız 3 tane marka bilgisini listede saklayınız .

x=input("Birinci marka")
y=input("İkinci marka")
z=input("Üçüncü marka")

list=[x,y,z]
print(list)
print(years)
print(names)
