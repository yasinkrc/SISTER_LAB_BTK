# def toplam (s1,s2):
#     print(s1+s2) hata veriri


# toplam(2,3,3)

# def method(*args):
#     print(list(args))

# method(1,2,3,"Selam","naber",1,3)

""" Elemanları teker teker göndermen lazım """

# def toplam (*args): 

#     toplam=0

#     for i in list(args) :
#         toplam+=i

#     print(toplam)

# # liste=[1,2,3,4,5,6,7,8,9,10]
# toplam(1,23,4,57)

# def func(**strVal):
#     print(type(strVal))
# func()

# def get_pers(**detail):
#     for data ,datay in detail.items() :
#         print(data,datay)

# get_pers(name="burak",surname="öztürk",age=29)

# def area(**values):
#     if "en" in values :
#         if "boy" in values :
#             return values["en"] *values["boy"]
#         else :
#             print("lütfen boy değerini girin")
#     else :
#         print("lütfen en ve boy değerlerinden birini girin")

# print(area(görev ="diktörgen hesaplama",en=15,boy=40))

# def func(strVal ,*args,**kwargs):
#     print(strVal)
#     print(args)
#     print(kwargs)

# func("Burak", 123 ,"Python","B",name="Burak",age=29)
