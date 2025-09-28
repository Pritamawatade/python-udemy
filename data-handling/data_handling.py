import csv
import os

FILE_NAME = 'contacts.csv'

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == name:
                print("contact already exists")
                return;

        with open(FILE_NAME, 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name,phone,email])
            print("contact added")

def read_contact():
    with open(FILE_NAME, 'r',encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # print(f"row = {row}")
            # print(f"{row["Name"]}\t {row["Phone"]}\t {row["Email"]}\t")
            # print(f"row name = {row["Name"]}")
            print(row["Name"])
            print(row["Email"])
            print(row["Phone"])

    print("Data printed successfully")



add_contact()
read_contact()