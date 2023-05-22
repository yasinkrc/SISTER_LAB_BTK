# def cube():

#     result=[]

#     for i in range(5):

#         result.append(i**3)
#     return result

# print(cube())

def cube():

    for i in range(5):
        yield i**3


# iterator=cube()

# for i in iter(iterator) :
#     print(i)




#İKİNCİ YOL 



# for i in cube() :
#     print(i)


genarator=(i**3 for i in range(5))
print(genarator)

# print( next(genarator))
# print( next(genarator))
# print( next(genarator))
# print( next(genarator))
# print( next(genarator))
# print( next(genarator))

for i in genarator :
    print(i)


"""generator=cube()

iterator=iter(generator)


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))"""