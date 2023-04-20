
"""value --> types"""

x=5
y=25

x=y
# print(x,y)
y=10
# print(x,y)

""" referance types => list """

a=["apple","banana"]

b=["apple","banana"]

a=b

b[0]="orange" #adres bilgileri taşınıyor 

print(a)
print(b)