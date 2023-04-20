sayılar =[1,3,5,7,9,12,19,21]

#1: sayılar listesini while ile ekrana yazdırın
# x=0
# while x<len(sayılar) :
#     print(sayılar[x])
#     x+=1
#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki  tüm tek sayıları ekrana yazdrın 
# ilk=int(input("başlangıç:"))
# son=int(input("son sayı :"))

# i =ilk

# while i<son :
#     i+=1
#     if(i%2!=0):
#         print(i)

      




#3: 1-100 arasındaki sayıları azalan şekilde yazdırın 
# ilk =1

# son =100

# while(son>=ilk) :
#     print(son)
#     son-=1
#4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın

# list =[]
# i=0
# while i<5 :
#     list.append(int(input(f"{i+1}.sayıyı giriniz")))
#     i+=1

# for x in list:
#     print(x)

#5: Kullanıcıdan alacağınız sınırsınız ürün bilgisini ürünler llistesi içinde saklayın
""" 

  ** ürün sayısını kulalnıcıya sorun .
  ** dictionary listesi yapısı (name , price ) şeklinde olsun 
  ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin 

  """
urunler=[]

adet=int(input("adet"))
i=0

while(i<adet):
    name=input("ürün ismi :")
    price=input("ürün fiyatı:")

    urunler.append({
        "name":name,
        "price":price

    })
    i+=1


for urun in urunler :
    print(f"urun adı : {urun['name']} urun fiyatı :{urun['price']}")
         
