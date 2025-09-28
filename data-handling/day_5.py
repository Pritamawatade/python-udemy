import csv
from collections import defaultdict
# import matplotlib
# matplotlib.use('') # Or 'Qt5Agg', 'Qt6Agg', etc.
import matplotlib.pyplot as plt

FILENAME = "weather_logs.csv"
def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["date"])
                temps.append(row["temp"])
                conditions[row["condition"]] += 1
            except:
                continue
    if not dates:
        print("NO data is available")
        return
    
    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker='o')
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("temperature_over_time.png")
    # plt.show()
    plt.close()

    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.savefig("weather_conditions.png")
    # plt.show()
    plt.close()


visualize_weather()