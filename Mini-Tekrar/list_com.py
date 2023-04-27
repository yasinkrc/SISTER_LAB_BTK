listNum=[1,2,3,4,56]
# print(listNum)

# listNum2=(a for a in range(20,41))
# print(listNum2)

# print(list(range(20,41))),

# kareList=[1,2,4,9,16,25]
# print(kareList)
# kareListV2=[a**2 for a in range(1,6)]
# print(kareListV2)

div1List=[num for num in range(1,52) if num%3==0]
print(div1List)
div2List=[num for num  in range(1,52) if num%2==0 and  num%6==0]
print(div2List)

# liste=[1,2,3,45,6,7,8,55,4,544,5,1,2,3,54,5,45,45,45,5,45,4,512,1,21,21,2,12,15]
# div3List=[n if n>=20 else "selam " for n in liste ]
# print(div3List)

# for num in range(1,51):
#     if num %2==0 and num %3==0:
#         print("sayı  2 ve 3 e bölünür ",num)
#     else :
#         print("sayı 2 ve 3 bölünmüyor",num)

meyveList=["elma","armut","kayısı","Şeftali"]

# meyveList2 =[meyve for meyve in meyveList]
# print(meyveList2)

meyveListV2 =[meyve.upper() for meyve in meyveList]
meyveListV2 =[meyve.capitalize() for meyve in meyveList]
meyveListV2 =[meyve.lower() for meyve in meyveList]
meyveListV2 =[meyve[0] for meyve in meyveList]


print(meyveListV2)
