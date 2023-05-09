# print("merhaba nasılsın\nBen iyim sen nasılsın ? ")

# isim ="Selam nasılsınız ben yasin ".split()

# result =isim.lstrip('ln')
# print(result)

# numbers=[(x,y )for x in range(1,5) for y in range(4,45)]
# print(numbers)

# for i in range(1,11) :
#     print(i,end=",")

""" fibonaci dizsi nedir
Fibonacci dizisi, 0 ve 1 ile başlayan ve her sayının kendisinden önceki iki sayının toplamı olduğu bir sayı dizisidir. Yani, dizinin ilk iki elemanı 0 ve 1'dir, sonraki elemanlar ise her zaman kendisinden önceki iki elemanın toplamıdır. Örneğin, Fibonacci dizisinin ilk birkaç elemanı şöyledir:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, ...
"""

def fibonacci(sayiKac):
    fibonacci_listesi = []
    ilksayi= 0
    ikincisayi =1
    for i in range(sayiKac):
        fibonacci_listesi.append(ilksayi)
        ilksayi = ikincisayi
        ikincisayi = ilksayi + ikincisayi
    return fibonacci_listesi


print(fibonacci(10))
        




    

    

