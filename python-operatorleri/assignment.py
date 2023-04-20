# x=5
# y=10 -> bunları böyle yazmak zor 
# z=20

x,y,z=5,10,20

# x,y=y,x
x+=5 #x=x+5
x-=5 #x=x-5
x*=5 #x=x*5
x/=5 #x=x/5
x%=5 #x=x%5
y//=5 #y=y//5
y**=5 #y=y**5
y**=z #y=y**z


# print(x,y,z)

values =1,2 ,3,4,5 #tuple de parantez zorunlu değil 

x,y,*z=values #olan değerler tam olmak zorunda 

print(values)
print(type(values))
print(x,y,z)