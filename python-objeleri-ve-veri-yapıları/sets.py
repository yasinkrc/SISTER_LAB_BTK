fruits={'orange','apple','banana'}

#print(fruits[0])--> indekselemez 

#sayısal inndeksseleme olamdığı için döngü kullanıyoruz 


for x in fruits:
    print(x)

 
fruits.add("cherry") #ekleme yapabilirisin 
fruits.update(["mango","grape"])
fruits.update(["mango","grape","apple"]) #her elemandan bir tane olmak zorunda 
fruits.remove("mango")
fruits.discard("apple")

fruits.pop() #kafasına göre siler ama diğerlerinde son elemanı silerdi
fruits.clear() #tüm elemanları siler 

print(fruits)

myList=[1,2,5,4,4,4,4,1,2,3,6,4,78,9,7,9]
print(set(myList)) #tekrarlanan elemanları düzenler ve sonradan da bunları buyuklüğe göre sıralar 
