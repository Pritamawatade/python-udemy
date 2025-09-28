import csv
from collections import defaultdict
import matplotlib
matplotlib.use("TkAgg")  # or "Qt5Agg"
import matplotlib.pyplot as plt


FILE_NAME = 'weather_logs.csv'

def visualize_weather():
    dates = []
    temps = []
    conditons = defaultdict(int)

    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                dates.append(row['date'])
                temps.append(row['temp'])
                conditons[row['condition']] += 1
            except:
                continue
            
        if not dates:
            print("No data is available")
        
        plt.figure(figsize=(10,7))
        plt.plot(dates, temps, marker='o')
        plt.title('Date and Temperature')
        plt.xlabel("Dates")
        plt.ylabel("Temperature")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(5,7))
        plt.bar(conditons.keys(), conditons.values(), color='skyblue')
        plt.xlabel("conditions")
        plt.ylabel("Days")
        plt.show()
        

visualize_weather()