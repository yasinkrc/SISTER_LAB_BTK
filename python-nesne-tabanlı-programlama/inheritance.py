#Inheritance (Kalıtım) : Miras alma 

#Person => name , lastname , age , eat() , run(), drink()

#Stundent(Person) , Teacher(Person)

# Animal - Dog (Animal),Cat (Animal) 

class Person():
    def __init__(self,fname ,lname) :
        self.firstname=fname
        self.lastname=lname
        print("Person created")
    def who_am_I (self):
        print("I am a person")
    def eat(self):
        print("I am eating ")
class Stundent(Person):
    def __init__(self,fname,lname,number):
       Person.__init__(self,fname,lname)
       self.stundentNumber=number
       print("Student Created")
       #overide 
    def who_am_I (self):
        print("I am a stundent")
    def sayHello(self):
        print("Say Hello")
class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname) #üste gider unutma 
        self.branch=branch
    def who_am_I(self):
        print(f"I am a {self.branch} teacher ")
p1=Person("Ali","Yılmaz")
s1=Stundent("Çınar","turan",18)
t1 =Teacher("Serkan ","Yılmaz","Doctor")



print(p1.firstname+"  "+p1.lastname)
print(s1.firstname+"  "+s1.lastname+" "+str(s1.stundentNumber))

p1.who_am_I()
s1.who_am_I()

p1.eat()
s1.eat()

s1.sayHello()