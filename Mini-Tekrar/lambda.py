# def func (num):
#     return num**2 

# print(func(5))

# func =lambda num : num**2

# print(func(2))

# func =lambda num1 , num2 : num1+num2

# print(func(3,6))

# func =lambda *num : sum (num)

# print(func(1,2,3,4,5,6,7,8,9))

# func =lambda *num : sum(num)

# print(func(6,466,6,4,6,4,56,4,6))

# def func(num1) :
#     return lambda num2 : num2*num1

# funcDoubler =func(2) #lambda num2 :num2*2
# funcTribler =func(3) #lambda num2 :num2*3

# print(funcDoubler(10))
# print(funcTribler(10))

mainFuction = lambda num ,subFunc : num +subFunc(num)

print(mainFuction(2 ,lambda x :x*2))
print(mainFuction(3 ,lambda x :x*2))
print(mainFuction(3 ,lambda x :x*x))
print(mainFuction(4 ,lambda x :x*x))