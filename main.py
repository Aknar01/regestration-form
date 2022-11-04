from RegistrationAndAuthentication import *

reg = RegistrationAndAuthentication("aknar","asanov",18, "aknar_03", "123456")
option = int(input("Select what do you want to do? \n"
                        "1. Register\n"
                        "2. Login\n"))

if option == 1:
    reg.register()
    reg.login()
elif option == 2:
    reg.login()
else:
    print("Oops! Try again")
