#def square(num): return num**2 

# result=square(2)
# print(result)
""" Lamda """

# numbers=[1,2,3,4,5]

# square=lambda num : num**2 
# result=list(map(square, numbers))
# result=square(3)
# print(result)

# for item in map(square ,numbers) :
#     print(item)

# square = lambda num : num**2 
numbers =[1,3,5,9,10,4]

check_even =lambda num : num%2==0 

# def check_even(num): return num%2==0

# result=list(filter(lambda num : num%2==0 ,numbers))
# result=list(filter(check_even , numbers))
result =check_even(numbers[0])
print(result)