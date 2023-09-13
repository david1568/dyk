password = "1568"

def zprava():
    print("dal si to")


password_input = input("password: ")
if password_input == password:
    zprava()
else:
    print("Zle Heslo")