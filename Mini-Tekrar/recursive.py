# def func1():
#     return 1

# def func2():
#     return 2

# def mainFunc():
#     print(func1())
#     print(func2())
# mainFunc()
# num =0
# def func():
#     global num  """ 997 kez çalışırlar recursive metotlar """
#     print(num)
#     num+=1
#     func()
    

# func()

""" Fonksiyonlar için verilen en iyi örneklerden biri olan Faktöriyelll :)"""


def faktr(sayi):

    if(sayi>1) :
         return  sayi*(faktr(sayi-1))
    else :
         return 1

   

print(faktr(100))