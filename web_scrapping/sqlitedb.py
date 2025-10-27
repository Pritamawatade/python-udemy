import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt
import schedule
import time
import sqlite3


API_URL = "https://api.coingecko.com/api/v3/coins/markets"
DB_NAME = 'crypto.db'
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS crypto_prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    coin TEXT,
                    price REAL
                )
                ''')
    conn.commit()
    conn.close()

def save_to_db(data):
    conn = sqlite3.connect(DB_NAME)    
    cur = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    for coin in data:
        cur.execute("INSERT INTO crypto_prices (timestamp, coin, price) VALUES (?,?,?)", (timestamp, coin["id"], coin['current_price']))
        
    conn.commit()
    conn.close()
    print("✅ data saved to database")

def search(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("select * from crypto_prices where coin = ? ORDER BY timestamp DESC LIMIT 1", (coin_name,))
    result = cur.fetchone()

    print(f"raw result: {result}")
    conn.close()

    
def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])
    print("✅ data saved to csv")


def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(float(row['price']))

    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()


def main():
   create_table()
   print("1. fetch and store data")
   print("2. search latest price of a coin")

   choice = input("Enter choice (1 or 2): ").strip()
   
   if choice == '1':
        print("Fetching live crypto data....")
        crypto_data = fetch_crypto_data()
        save_to_csv(crypto_data)
        save_to_db(crypto_data)

        print("-" * 30)
        for coin in crypto_data:
            print(f"{coin['id']} - ${coin['current_price']}")
        print("-" * 30)

        coin_choice = input("Enter the coinname to get graph: ").strip().lower()

        if coin_choice:
            plot_graph(coin_choice)
   elif choice == '2':
        coin_name = input("Enter the coin name to search: ").strip().lower()
        search(coin_name)
   else:
        print("Invalid choice. Exiting.")
    

if __name__ == "__main__":  
    main()
