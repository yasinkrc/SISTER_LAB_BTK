#key - value 

# 41 => Kocaeli , 34 => İstanbul

sehirler =["kocaeli","istanbul"]

plakalar =[41,34]

print(plakalar[sehirler.index("kocaeli")])
# print(plakalar[sehirler.index("istanbul")])

""" Ne istiyoruz """
#print(plakalar["kocaeli"]) --> 41
#print(plakalar["isatnbul"]) --> 34 


""" plaklar ={'key' : 'value'} """

plakalar={'kocaeli':41,'istanbul':34}

print(plakalar["kocaeli"])

print(plakalar["istanbul"])



plakalar["ankara"] =6

""" {'kocaeli': 41, 'istanbul': 34, 'ankara': 6} """ 
#çıktısı böyle olur bu da demek ki veri ekleme çıkarma oluyormus tuple olmuyordu 
plakalar['kocaeli']="new value"
""" {'kocaeli': 'new value', 'istanbul': 34, 'ankara': 6} """
#çıktısı böyle olur bu da demek ki veri güncleme  oluyormus tuple olmuyordu 
print(plakalar)


users ={
    'sadikturan':{
    'age':36,
    'email':'sadik@gmail.com',
    'address':'kocaeli',
    'phone':'123456789'
                  }, 
    'cinarturan':{
    'age':2,
    'roles':["admin","user"],
    'email':'cinar@gmail.com',
    'address':'kocaeli',
    'phone':'123456789'
                  }, 
}
print(users["cinarturan"]['age'])
print(users["cinarturan"]['phone'])
print(users["cinarturan"]['roles'][0])