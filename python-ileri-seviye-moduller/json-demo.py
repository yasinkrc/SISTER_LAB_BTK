import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users :
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user["password"],email=user["email"])
                    self.users.append(newUser)
                print(self.users)
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        self.loadUsers()
        print("Kullanıcı oluşturuldu")

    def login(self,username,password):
        
        for user in self.users :
            if user.username==username and user.password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print("Login yapıldı")
                break
    
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("Çıkış Yapıldı")
    
    def identity(self):
        
        if self.isLoggedIn :
            print(f"ysername : {self.currentUser.username}")
        else :
            print("Kullanıcı giriş yapılmadı")
       
    def savetoFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(liste, file)

repository = UserRepository()

while True:
    print("MENÜ".center(50, "*"))
    choice = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")
    
    if choice == '5':
        break
    else:
        if choice == '1':
            # Register
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user = User(username, password, email)
            repository.register(user)
           
            
        elif choice == '2':
            # Login
            if repository.isLoggedIn:
              print("zaten login olddunuz ")
            else :
                username=input("username")
                password=input("password")
                repository.login(username,password)
        elif choice == '3':
           pass
        elif choice == '4':
            repository.identity()
        else:
            print("Yanlış seçim")
