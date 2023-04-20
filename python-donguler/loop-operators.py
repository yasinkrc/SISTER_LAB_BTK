""" range """

# list =[1,2,3]

# print(list)

# for x in list :
#     print(x)
# for item in range(10):
#     print(item)
# for item in range(2,10):
#     print(item)
# for item in range(5,100,5):
#     print(item)

# print(list(range(5,100,5))) #listeye çevirme işlemi .

"""  enumerate """
# index=0
# greeting ="Hello word"

# for letter in greeting:
#     print(f"index:{index} letter {letter}")
#     index+=1
# greeting ='Hello word '

# for item in enumerate(greeting):
#     print(item)
# """  zip """

# list1 =[1,2,3,4,5]

# list2 =['a','b','c','d','e']

# list3=[100,200,300,400,500]

# for item in zip(list1,list2,list3) :

#     print(item )

# for a,b,c in zip(list1,list2,list3) :

#     print(a)
#     print(a,b,c)

# print(list(zip(list1,list2,list3)))


""" zip """

list1 =[1,2,3,4,5]

list2=["a","b","c","d","e"]

print(tuple(zip(list1,list2)))