import base64
import os

VAULT_FILE = 'vault.txt'

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()
    
def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_<>" for c in password)

    score = sum([length >= 8, has_digit, has_special, has_upper])

    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credential():
    username = input("Enter username : ").strip()
    password = input("Enter paassword : ").strip()
    website = input("Enter website : ").strip()

    strength = password_strength(password)  
    line = f"{website} | {username} | {password}"
    encoded_line = encode(line)
    
    with open(VAULT_FILE, 'a') as f:
        f.write(f"{encoded_line}\n")

    print(f"Credential added for {website}. Password strength: {strength}")     

def view_credentials(): 
    if not os.path.exists(VAULT_FILE):
        print("Data do not exits")

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            print(f"decoded line: {decoded}     ")
            website, username, password = decoded.split("|")
            hidden_password = '*' * len(password)
            print(f"{website}| {username} | {hidden_password}")

def main():
    while True:
        print(f"Enter Your credential :  \n1. Add Credential\n2. View Credential\n3. Exit")
        choice = input("Enter your choice : ").strip()      
        if choice == '1':
            add_credential()
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")      
    print("Exiting...") 
    
if __name__ == "__main__":
    main()
    


    



