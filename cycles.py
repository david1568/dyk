# for i in range (cyklus v počtu akým chceš)
list1 = [1, 2, 3, 4, 5]

i = 0
for i in range(4):
    print(list1[i])
    i =+ 1

#while (slúži ako opakovačka pod nejakou podmienkou pokial nebuďe splnená)
username = "Admin"
password = "1568"

i = 0

while i == 0:
    u_input = input("username: ")
    p_input = input("password: ")
    if u_input == username and p_input == password:
        break
    else:
        print("Špatné Heslo")

#for vec in (cyklus ktorý sa stane pre každý prvok v liste)
list2 = [1, 2, 3, 4, 5]

for item in list2:
    print(item)