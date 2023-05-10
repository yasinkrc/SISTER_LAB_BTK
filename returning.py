# def usalma(number):
#     #two=usalma(2)
#     #three=usalma(2)

#     def inner(power):
#         return number**power
    
#     return inner

# two=usalma(2)

# three=usalma(4)

# print(two(3))
# print(three(3))


# def yetki_sorgula(page):

#     def inner (role):

#         if role == "Admin":
            
#             return f"{role}  rolü {page} sayfasına ulaşabilir "
#         else :
#              return f"{role}  rolü {page} sayfasına ulaşamaz "
#     return inner

# admin_user = yetki_sorgula("product Edit")

# print(admin_user("Admin"))

# print(admin_user("User"))

def islem(islem_adi):

    def toplam(*args):
        toplam=0

        for i in args :

            toplam +=i
        return toplam 
    def carpma (*args) :
        carpim =1 

        for i in args :

            carpim*=i
        
        return carpim 
    
    if islem_adi=="toplama":
        return toplam
    
    else :
        return carpma


toplama=islem("toplama")
print(toplama(1,5,6,4,9,46,56,6,46))
toplama=islem("lafjh")
print(print(toplama(1,5,6,4,9,46,56,6,46)))