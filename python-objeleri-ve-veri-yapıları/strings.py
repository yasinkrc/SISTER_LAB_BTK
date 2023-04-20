name="Sadık"
surname="Turan"
age=36

# print("My name is "+name +" "+surname+" and \n  I am "+str(age)+ " years old .")
greeting = "My name is "+name +" "+surname+" and   I am "+str(age)+ " years old ."
length =len(greeting)
print(greeting)

print(greeting[0]) #ilk eleman 

print(greeting[3]) #3.eleman ama dikkat 0.indeksten başlarlar 

print(len(greeting)) #dizinin kaç elemanlı olduğunu belirtir 

print(greeting[length-1]) #bize dizinin son elemanını verir 

print(greeting[-1]) #bize dizinin son elemanıdan önceli elemanı verir 

print(greeting[2 : 5 ]) 

print(greeting[3 : ]) #3. elemandan son elemana kadar 

print(greeting[: 15 ]) #baştan 15. elemana kadar 

print(greeting[2 :40 :2]) #2.elemandan 40.elemana kadar ama her iki adımda al 


print(greeting[::]) #tüm elemanları alır 
print(greeting[::-1]) #tüm elemanları alır ama tersten alır 
