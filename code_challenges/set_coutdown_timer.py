import time     

def take_input():
    while True:
        user_input = input("Enter the time in seconds for countdown: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer.")
            
print("Countdown Timer")
seconds = take_input()

for i in range(seconds, 0, -1): 
    mins, seconds = divmod(i, 60)
    time_format = f"{mins:02}:{seconds:02}"
    print(time_format, end="\r")
    time.sleep(1)
print("Time's up!") 