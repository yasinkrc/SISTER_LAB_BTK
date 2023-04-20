sayilar =[1,3,5,7,9,12,19,21]

#1- Sayilar listesindeki hangi sayılar 3'ün katıdır

# for i in sayilar :
#     if(i%3==0):
#         print(i)

#2- Sayılar listesindeki sayıların toplamı kaçtır 
# topla=0
# for i in sayilar :
#      topla+=i
# print(topla)
#3- Sayılar listesindeki tek sayıların karesini alınız 
# for i in sayilar :
#      if(i%2!=0):
#           print(i**2)
    

sehirler =["kocaelli","istanbul","ankara","izmir","rize"]


#sehirlerden hangileri en fazla 5 karekterlidir 
# for i in sehirler :
#     if(len(i)<=5):
#         print(i)


urunler = [
  {'name':'samsung S6', 'price':'3000' },
  {'name':'samsung S7', 'price':'4000' },
  {'name':'samsung S8', 'price':'5000' },
  {'name':'samsung S9', 'price':'6000' },
]

#ürünlerin toplam fiyatı nedir 
fiyat=0
for urun in urunler:
    fiyat+=int(urun['price'])
print(fiyat)