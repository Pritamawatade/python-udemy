import datetime


message = input("Enter your journal entry: ").strip()
rating = input("Enter your rating (1-10)(optional): ").strip()


now = datetime.datetime.now();

datestr = now.strftime("%Y-%m-%d %I:%M %P")

journal_entry = f"\n date:{datestr}\n message:{message}\n rating:{rating}\n {'*' * 20}"

with open("learnings.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print("Journal entry added.")
