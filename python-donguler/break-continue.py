name ="Sadik Turan"

# for letter in name :
#     if letter =='a':
#         break
#     print(letter)

# for letter in name :
#     if letter=='i':
#         continue
#     print(letter)
    
""" önemli nokta """
# x=0

# while x<5 :
#     x+=1  
#     if x==2 :
#         continue
#     print(x)
    
x=1 
result =0

while x<=100 :
    x+=1
    if x%2==1 :
        continue
    result+=x
    
print(f"toplam : {result}")
while x<=100 :
    x+=1
    if x%2==0 :
        continue
    result+=x
    
print(f"toplam : {result}")