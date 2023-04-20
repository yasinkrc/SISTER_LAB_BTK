numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val =min(numbers)
val=max(numbers)
val=min(letters)
val=max(letters) #alfabede kim önce geliyor 

val =numbers[3:6]
val=numbers[:3]
val=numbers[4:]
numbers[4]=40

numbers.append(49) #sona eleman ekler 
numbers.append(59)

numbers.insert(3,78) #istediğimiz alana yükler 

numbers.insert(-1,52) #Burda dikkat edilmesi gereken bi nokta var bunun çıktısında 
""" [1, 10, 5, 78, 16, 40, 9, 10, 49, 52, 59]  """ #52 sonda değil çünkü en sondaki indeksin koltığuna oturuyor bu yuzden diğeri sola kayıyor 
numbers.pop() #sondaki elemanı siler 
numbers.pop(0) #indeks verisen de istediğin değeri siler 
numbers.remove(49) #burda da direk değeri veriyorsun ve siliyor 

numbers.sort() #değerleri sıralar digit olarak 
letters.sort() #değerleri sıralar alpahatik  olarak 

""" Eğer tam tersine çevirmek istersen de reverse() methodunu kullan """

numbers.reverse()
numbers.sort() 

print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count("a"))
val=numbers
# val=letters

numbers.clear() #Tüm elemanları siler 

print(val)