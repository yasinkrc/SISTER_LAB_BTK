# x ="global x "

# def function():
#     x="local x"

#     print(x)

# function()
# print(x)
# """ global """
name ="Çınar"

def changeName(new_name):
    """ local """
    global name 
    name=new_name
    print(name)


changeName("ada")
# print(name)

# name ="global string "

# def greeting ():
#     # name ="Çınar"

#     def hello() :
#         # name="Ada"
#         print("hello"+name) #bir üstteki fonkisyon ele alındı 

#     hello()
# greeting()
# print(name)

x=50 
def test():
    global x 
    print(f"{x}")

    x=100 
    print(f"changed x to {x} " )

test()
print(x)