import os
import json






INPUT_FILE='flatton.json'
OUTPUT_FILE='flattoned_data.json'

def flatten_data(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k,v in data.items():
            full_keys =  f"{parent_key}{sep}{k}" if parent_key else k
            print(full_keys)
            items.update(flatten_data(v, full_keys, sep=sep))
    elif isinstance(data, dict):
        for idx, item in enumerate(data):
            full_keys = f"{parent_key}{sep}{idx}" if parent_key else str(idx)    
            items.update(flatten_data(item, full_keys, sep=sep))
    else:
        items[parent_key] = data
    
    return items



def main():
    if not os.path.exists(INPUT_FILE):
        print("no file found")
        return
    
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        sep = input("Enter your sepator ex .,/ : ").strip() or '.'

        flattened = flatten_data(data, sep=sep)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(flattened,f, indent=2 )

        print(f"File saved successfully")

        
    except Exception as e:
        print(f"something went wrong while converting data {e} ")


if __name__ == '__main__':
    main()

