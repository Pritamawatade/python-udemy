seat_type = input("Enter seat type, AC/general/sleeper:  ").lower()

match seat_type:
    case "sleeper":
        print("NO AC, beds availble")
    case "general":
        print("general seat, no seat, can't guranteed")
    case "AC":
        print("AC availble ENJOY")
    case _:
        print("default case")

print(f"seat_type = {seat_type}")
