name ="Çınar"
surname ="Turan"
age=25

# print("My name is {}".format(name ,surname)) #Sadece çınarı alır 
# print("My name is {1} {0}".format(name ,surname)) #direk indeks numaralarıyla da ulaşabilirsiniz 
# print("My name is {n} {s}".format(n=name ,s=surname)) 
print("My name is {n} {s} and I am {a} years old ".format(n=name ,s=surname ,a=age ))
print("My name is {} {} and I am {} years old ".format(name , name , name  ))

#Dikkat !!!  eğer format içindeki parantezlere bir şey yazarsan unutma hespine yazmak gerek .

result =200/700

print("the result is {r:1.5}".format(r=result))

print(f"My name is {name} {surname} and I am {age} years old.") #dikkat 
