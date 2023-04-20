#eğer for bilmezek çok fazla satır kod yazmak zorunda kalacağız 

numbers =[1,2,3,4,5]

for num in numbers :
    print(num)
  # print("hello")

names=["Çınar","Sadık","Sena"]

for name in names :
    print(f"my name is {name}")

name="sadık turan"

for n in name :
    print(n)

# tuple=(1,2,3,4,5)
tuple =[(1,2,),(1,3),(3,5),(5,7)]

for t,b in tuple :
    print(t)


d={'k1':1 , 'k2':2 ,'k3':3}

for key , value  in d.items() :
    # print(key)
    print(value)