""" Aşağıdaki soruları cevaplayınız . """

website ="http://www.saddikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- 'course' karekter dizisinde kaç karekter bulunmaktadır ?

result =len(course)

#2- 'website' içinden www karekterlerini alın .

website=website[0 :7]+website[10:]
result=website
#3- 'website' içinden com karekterlerini alın .

x=len(website)
website =website[:x-3]
result=website

#4- 'course' içinden ilk 15 ve son 15 karekterlerini alın . 


result=course[:15]+course[-15 :]

#5- 'course' ifadesindeki karekterleri tersten yazdırın  .

result=course[::-1]

print(result)

name , surname , age , job = "Bora" , "Yılmaz" , 32 ,"Mühendis"

#Yukarıdaki verilen  değişkenler ile ekrana aşağıdaki ifadeyi yazdırınız .
""" Benim adım  Bora Yılmaz , Yaşım 32 ve mesleğim mühendis."""

print(f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}")

#7 ' Hello world ' ifadesindeki w harfini "W" ile değiştirin 

ad="Hello world"
ad =ad[:5]+" W"+ad[7:]

#8  'abc' ifadesini yan yana 3 defa yazdırın .

ad="abc"*3


print(ad)

