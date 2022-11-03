master_pwd = input("What is the master password?: ")


def view():
    pass

# menu
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode.lower() == "view":
        pass
    elif mode.lower() == "add":
        pass
    elif mode.lower() == "q":
        break
    else: 
        print("Invalid mode.")
        continue