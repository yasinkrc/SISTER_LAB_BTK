x=6 
hak =5
devam='e'
result=5<x<10 

#and &&
result = (x>5) and (x<10)
result=(hak>0)and(devam=='e')

#or || 

result=(x>0) and (x%2==0)

#not ! 

result=(x>0)

# X , 5 ve 10 arasında bir çift sayı  mı ? 
result=(x>5) and (x<10) and (x%2==0)

print(result)
