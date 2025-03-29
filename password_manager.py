password = input("What is the master password? ")

def view():
    with open('passwords.txt', "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "- Password:", passw)

def add():
    name = input("Account name: ")
    password = input("Password: ")

# w --> write/overwrite
# r --> read
# a --> append (add smth at the end of the file and create a new file if that file does not exist)
    with open('passwords.txt', "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press Q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode')
        continue