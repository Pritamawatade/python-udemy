import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = 'vault.json'
KEY_FILE = 'vault.key'

def load_or_crete_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
            
    return Fernet(key)


fernet = load_or_crete_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
        


def save_vault(data):
    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)    

        
def add_note():
    title = input("Enter note title :").strip()
    content  = input("Enter note content :").strip()

    encrypted_key = fernet.encrypt(content.encode()).decode()
    timestamps = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title":title,
        "content": encrypted_key,
        "timestamp": timestamps
    })
    
    save_vault(data)
    print("Data saved")

def list_note():
    data = load_vault()
    if not data:
        print("No data availble to print")
        return []
    
    for i, item in enumerate(data):
        print(f"{i} {item['title']} | {item['timestamp']}")


def view_note():
    list_note()
    try:
        index = int(input("Enter index of the note"))
        print(f"index = {index}")
        data = load_vault()
        print(f"data = {data}")
        print(f"data length = {len(data)}")
        
        if 0<= index < len(data):
            print(f"Valid index {index}")
            print(f"data at index tile {data[index]['content']}")
            print(f"data at index {data[index]}")
            encrypted_content = data[index]['content']
            # print("Decrypted content :", decrypted_content  )
            decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
            
            
            print(f"\n {data[index]['title']} {data[index]['timestamp']}\n\n {decrypted_content}")
        else:
            print("Invaild selection.")
    except:
            print("Invalid input")


def main():
    while True:
        print("Cryptography Fernet : ")
        print("1. Add Note")
        print("2. List Note")
        print("3. View Note")
        print("4. Exit")    
        
        choice = input("Enter your choice :").strip()
        if choice == '1':
            add_note()
        elif choice == '2':
            list_note()
        elif choice == '3':
            view_note()
        elif choice == '4':   
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":      
    main()  

