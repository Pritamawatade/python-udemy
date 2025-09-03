voters = [(15,"pritam"),(16,"venky"),(12,"amol"),(11,"Hitesh")]

for age,name in voters:
    if age >= 18:   
        print(f"{name} is eligble for vote")
        break
    
else:
    print("we entered into the else block of loop")
