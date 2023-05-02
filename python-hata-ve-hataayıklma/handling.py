#error handling => hata yönetimi 

# try :
#     x=int(input("x :"))
#     y=int(input("y :"))
#     print(x/y) 
# except (ZeroDivisionError , ValueError  ) as a :
#     print("yanlış bilgi girdiniz  ")
#     print(a) #print(a)
while True :
    try :
        x=int(input("x :"))
        y=int(input("y :")) 
        print(x/y) 
    except Exception as a :
        print("yanlış bilgi girdiniz  ")
    else :
        break
    finally :
        print("try except sonlandı")








