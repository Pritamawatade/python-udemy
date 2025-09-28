''''


'''

import csv
import os
from datetime import datetime
import requests


FILE_NAME = "wether_logs.csv"

city = ""
APIKey = "put-your-own-key-here" # get your own key from openweathermap.org


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        writer.writerow(["date", "city", "temp", "condition"])
        

def log_wehter():
    city = input("enter your city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")
    print(f"fetching data for {city} on {date}")

    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        print("reader = ", reader)
        
        for row in reader:
            print("row = ", row)
            if row['date'] == date and row['city'] == city:
                print("duplicate entry, city data for same day already exists")
                return
        
    try:
        print("Entered in ty block")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("API filed with status code ", {response.status_code})
            return
        
        temp = data["main"]['temp']
        condition = data["weather"][0]["main"]
        with open(FILE_NAME, 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print("data inserted successfully")

        
    except Exception as e:
        print("something went wrong while making request")
      
def view_all_records():
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(f"\n{row['date']} {row['city']} {row['temp']} {row['condition']}")  
            
def search_by_city():
    city = input("Enter city name: ")
    print("city = ", city)

    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if city.lower() == row['city'].lower():
                print(f"\n{row['date']} {row['city']} {row['temp']} {row['condition']}")
                return
    print("no records found for city ", city)
        
def main():
    
    while True:
        print("\n\nReal time weather logger: \n")
        print('1. add weather\n 2.view all records\n 3.search city\n')
        option = input("Enter your choice: ")
        
        match(option):
            case '1': log_wehter()
            case '2': view_all_records()
            case '3': search_by_city()
            case _: print("Wrong choice")
            

if __name__ == '__main__':
    main()