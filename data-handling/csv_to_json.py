import json 
import csv
import os

INPUT_FILE='contacts.csv'
OUTPUT_FILE='converted_data.json'

def load_csv_data():
    if not os.path.exists(INPUT_FILE):
        print("CSV file not found")
        return []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(f"data = {reader}")
        return data
    
def save_as_json(data, filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"converted {len(data)} in to {filename}")


def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))
        print('....')

def main():
    data = load_csv_data()
    if not data:
        return
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == '__main__':
    main()