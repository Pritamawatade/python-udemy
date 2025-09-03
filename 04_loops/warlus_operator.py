# Without warlus operator code is
value = 3
reminder = value % 5

if reminder:
    print(f"not devisible reminder = {reminder}")

if (reminder := value % 5):
    print(f"not devisible reminder = {reminder}")

sizes = ["small", "medium", "large"]

if (req_size := input("enter the prefered size:") in sizes):
    print(f"your choice is {req_size}")
else:    
    print(f"your choice is not available {req_size}")
