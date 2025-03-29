from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_password = input("What is the master password? ")
key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "- Password:", str(fer.decrypt(password.encode())))


def add():
    name = input("Account name: ")
    password = input("Password: ")

# w --> write/overwrite
# r --> read
# a --> append (add smth at the end of the file and create a new file if that file does not exist)
    with open('passwords.txt', "a") as f:
        f.write(name + "|" + str(fer.encrypt(password.encode())) + "\n")

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