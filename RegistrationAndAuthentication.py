from hashlib import md5
import json

class RegistrationAndAuthentication:
    def __init__(self, name, surname, age, username, password):
        self.__name = name.capitalize()
        self.__surname = surname.capitalize()
        self.__age = age
        self.__username = username
        self.__password = self.hash_password(password)

    f = open('db.json', "r")
    jF = json.load(f)
    f.close()

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__name
    def set_surname(self, surname):
        self.__surname = surname

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def get_username(self):
        return self.__name
    def set_username(self, username):
        self.__username = username

    def get_hashPass(self):
        return self.__password
    def set_hashPass(self, password):
        self.__password = self.hash_password(password)

    def register(self):
        name = input("Your name: ")
        surname = input("Your surname: ")
        age = int(input("Your age: "))
        if age > 0 and age < 100:
            pass
        else:
            print('you entered the wrong age')
            self.register()
        username = input("Login: ")
        for item in self.jF["items"]:
            if username in item["username"]:
                print("This username is already taken")
                return self.register()

        password = input("Password: ")
        verifyPass = input("Verify password: ")
        if password == verifyPass:
            print('you have successfully registered')
            password = self.hash_password(password)
        else:
            print("passwords don't match,repeat again")
            self.register()

        newUser = {
            "username": username,
            "password": password,
            "name": name,
            "surname": surname,
            "age": age
             }
        self.jF["items"].append(newUser)
        with open("db.json", "w") as new:
            json.dump(self.jF, new)


    def login(self):
        username = input("Login: ")
        password = input("Password: ")
        for item in self.jF["items"]:
            if username == item["username"] and md5(password.encode()).hexdigest() == item["password"]:
                print(f'Your name: {item["name"].capitalize()}')
                print(f'Your surname: {item["surname"].capitalize()}')
                print(f'Your age: {item["age"]}')
                chPass = int(input("To change the password, enter the '1': "))
                if chPass == 1:
                    self.change_password()
                return
            elif username == item["username"] and md5(password.encode()).hexdigest() != item["password"]:
                print('incorrect password')
                self.login()
                break
            else:
                print('There is no such login')
                self.login()

    def change_password(self):
        oldPass = input('Enter the old password:')
        for item in self.jF["items"]:
            if md5(oldPass.encode()).hexdigest() == item["password"]:
                newPass = input('Enter the new password: ')
                item["password"] = md5(newPass.encode()).hexdigest()
                with open("db.json", "w") as nPass:
                    json.dump(self.jF, nPass)
                print("Successfully updated!")
                return
        print("you entered the password incorrectly")
        self.change_password()


    def hash_password(self, password):
        return str(md5(password.encode()).hexdigest())



