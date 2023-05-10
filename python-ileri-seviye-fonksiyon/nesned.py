# def greeting(name):
#     print("hello",name)


# # greeting("ali")
# # print(greeting)

# sayHello=greeting

# print(sayHello)
# print(greeting)

# del sayHello 

# print(greeting)

#encapsulation
# def outer (num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1+1
#     num2= inner_increment(num1)
#     print(num1,num2)

# print(outer(10))

# print(inner_increment(10))

def factorial(number):

    if not isinstance(number,int):

        raise TypeError("number must be an integer")
    if not number >=0 :
        raise ValueError ("number must be an integer")
       
    def inner_factorial(number):
        if number <=1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

try :
    print(factorial(-8)) 
except Exception :
    print("yanlış  hata ")

finally :
    print("kod bitti ")