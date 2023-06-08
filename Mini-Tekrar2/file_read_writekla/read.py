f=open("blabla.txt","r")

# print(f.read())
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# f.seek(0)
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")


# print(f.readlines())

toplam =[]
for satir in f :
    # print(satir,end="")
    ogr=satir.split(":")
    toplam.append(ogr[0])

f.close()
print(toplam)

top=0
for i in toplam :

    top=top+int(i)

print(top)
