
website ="http://www.saddikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1-' Hello World ' karekter dizisinin baş ve sondaki karekterlerini silin .
result=' Hello World '.strip()
result=' Hello World '.lstrip()
result=' Hello World '.rstrip()

result=website.lstrip("/:pth") #dikkat et ortada bir sayı verme sol da ise sol sağ da ise sağ ver 
#2-'www.sadikturan.com' içindeki sadıkturan bilgisi haricindeki her karekteri silin .
result='www.sadikturan.com' 
result=result.strip("w.moc") 
#3-'course' karekter dizisinin yüm karekterlerini küçük harf yapın  

result=course.upper()
result=course.capitalize()
result=course.title()
result=course.lower()

#4-'Website' içinde kaç a karekteri vardır ? (count("a"))

result=website.count("a")
result=website.count("www")
result=website.count("www",0,10)

#5-'website' www ile başlayıp com ile bitiyor mu ?
result=website.startswith("www") and website.endswith("com")
#6-'website' içinde '.com' ifadesi var mı ? 
result=website.find(".com")
result=website.find(".com",10,2)
result=course.find("Python")
result=course.rfind("Python") #find methoduna alternatif bir method var 

result=website.index("com") #bulmazsa hata veriri find dan farkı budur 
result=website.rindex("com") 
# result=website.rindex("com") #bunun için biz ileride exception denen bir kavram var biz onu kullanacağız 

#7-'course' içindeki karekterlerin hepsi alfabetik mi (isalpha , isdigit)
result=course.isalpha()
result="Hello".isalpha()
result="course".isdigit()
result="123".isdigit()
#8-'Contents' ifadesini satırda 50 karekter içine yerleştirip sağ ve soluna * ekleyiniz .

result="Contents".center(50,"*")

#9-'course' karekter dizisindeki tüm boşluk karekterlerini '-' ile gösterin 
result=course.replace(" ","-")
result=course.replace(" ","-",5)
rresult=course.replace("  "," ")

#10-'Hello World' karekter dizisinin "World" ifadesini "There" olarak değiştirin .

result="Hello World".replace("World","There")

#11-'course' karekter dizisini boşluk karekterlerinden ayırın . 

result=course.split(" ")
# result=result[2]
result=result[5]


print(result)