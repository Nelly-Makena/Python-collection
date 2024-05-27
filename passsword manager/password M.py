from cryptography.fernet import Fernet # type: ignore

def write_key():
   
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)



def load_key():
   
    
    return open("key.key", "rb").read()

master_pwd = input("What's your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, encrypted_pass = data.split("|")
            decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
            print("User:", user, "| Password:", decrypted_pass)

def add():
   
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to view existing passwords or add new ones? (view/add) Press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please choose 'view' or 'add'.")
