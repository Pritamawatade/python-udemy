import csv
import json
import os

INPUT_FILE='api_data.json'
OUTPUT_FILE='converted.csv'

def load_json_data(filename):
    
    if not os.path.exists(filename):
        print("FILE not found")
        return []
    
    with open(filename, 'r', encoding='utf-8') as f:
        
        try:
            return json.load(f)
        except:
            print("File is invalid json format")


def convert_to_csv(data, outputfile):
    if not data:
        print("No data to convert")
        return
    
    feild = list(data[0].keys())

    with open(outputfile, 'w', encoding='utf-8')as f:
        writer = csv.DictWriter(f, fieldnames=feild)
        writer.writeheader()
        
        for row in data:
            writer.writerow(row)
    
    print(f"{len(data)} inserted successfully")


def main():
    print("converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)


if __name__ == "__main__":
    main()