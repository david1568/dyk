# Login Test

# Admin Udaje
username = "Admin"
password = "1568"

# User Udaje
username_input = input("username: ")
password_input = input("password: ")

# System
if username == username_input and password == password_input:
    print("Fachčito")
elif username == username_input and password != password_input:
    print("Zlé Heslo")
elif username != username_input and password == password_input:
    print("zlé username")
