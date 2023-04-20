"""
Daire alanı  :  πr2
Daire çevresi : 2πr 


*Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız ? (r::3.14)


"""

pi=3.14 

r=int(input("yarı çap : " ))

alan =pi*(r**2)

cevre=2*(pi*r)

print("alan : ",alan)
print("cevre : ",cevre)