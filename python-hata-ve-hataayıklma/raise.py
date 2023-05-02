# x=10 

# if x>5  :
#     raise Exception("X 5'den büyük değer alamaz")
    

# def check_password(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("parola en az 7 karekter olmalıdır ")
#     elif not re.search("[a-z]",psw):
#         raise Exception ("parola küçük harf içermelidir")
#     elif not re.search("[A-Z]",psw):
#         raise Exception ("parola büyük harf içermelidir")
#     elif not re.search("[0-9]",psw):
#         raise Exception ("parola rakam içermelidir")
#     elif not re.search("[_@$]",psw):
#         raise Exception ("parola alpha numeric karekter  içermelidir")
#     elif re.search("/s",psw):
#         raise Exception("parola boşluk içermemlidir")
#     else :
#         print("tebrikler parola doğru")

# password=input("parolanızı giriniz")

# try:
#     check_password(password)
# except Exception as ex:
#      print(ex)
# else :
#     print("geçerli parola ")
# finally :
#     print("validation geçerli")

class Person :

    def __init__(self,name ,year) :
        if len(name)>10 :
            raise Exception ("name alanı fazla karekter içeriyor")
        else :
            self.name=name
            self.year=year

p=Person("yasinkaraca",1222)