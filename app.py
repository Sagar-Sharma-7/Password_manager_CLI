master_pwd = input("What is the master password?: ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: ", user, "| Password: ", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

# menu
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    elif mode.lower() == "q":
        break
    else: 
        print("Invalid mode.")
        continue