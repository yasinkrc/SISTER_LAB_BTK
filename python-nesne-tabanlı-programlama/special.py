myList=[1,2,3]
myString ="My string"

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi oluşturduk")

    def __str__(self):
       return (f"{self.title} by {self.director}")
    def __len__(self):
        return self.duration
    def __del__(self):
        return "  film Objesi silindi"


m=Movie("filmadı","yönetmeb adı",120)

# print(type(m))  
# print(len(m))

# print(str(myList))
print(str(m))

# print(len(myList))
# print(len(m))

# del m

# print(m)