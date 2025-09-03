for i in range(1,10):   # here instaed of range method it can be any iterable object like string, touple, list etc.
    print(i)

print("\n2 step size")
for i in range(1,10, 2):  # here 2 is the step size
    print(i)

print("1 step size")
for i in range(10, 0, -1):  # here -1 is the step size
    print(i)

print("\n2 step size")
for i in range(10, 0, -2):  # here -2 is the step size
    print(i)


# looping thourgh list

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

for hero in heros:
    print(f"hero = {hero}")


# looping with enumerate

for index, hero in  enumerate(heros, start=1):
    print(f"{index}:{hero}")