

# with open("newfile.txt","r+",encoding="utf-8") as file :
#     file.seek(20)
#     file.write("deneme")
    
# with open("newfile.txt","r+",encoding="utf-8") as file :
#     print(file.read())

"""  Sayfa sonunda günceleme """
# with open("newfile.txt","a",encoding="utf-8") as file: 
#     file.write("/n Emel Turan")


"""  Sayfa başında  günceleme """ 
# with open("newfile.txt","r+",encoding="utf-8") as file :
#     content=file.read()
#     content="Efe Turan \n"+content
#     file.seek(0)

#     print(content)

"""  Sayfa ortasında  günceleme """ 


with open("newfile.txt","r+",encoding="utf-8") as file :
    list=file.readlines()
    help(list.insert)
    list.insert(1,"Ali Korkmaz \n ")
    file.seek(0)
    file.writelines(list)
    # for i in list :
    #     file.write(i)

with open("newfile.txt","r",encoding="utf-8") as file :
    print(file.read())
