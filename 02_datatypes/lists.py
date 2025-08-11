heros = ['superman', 'batman', 'spiderman', 'ironman']
heros.append('hulk')
print(heros)

heros2 = ['captain  america', 'antman']
print(f"heros2={heros2}")

heros.extend(heros2)
print(f"heros={heros}")

heros.insert(2, 'thor')
print(f"heros={heros}")

heros.reverse()
print(f"reversed_heros={heros}")
heros.sort()
print(f"sorted_heros={heros}")

print(heros[::2])  # every second hero
print(heros[1:4])  # heroes from index 1 to 3
print(heros[-1])   # last hero
print(heros[-2:])  # last two heroes

heros.remove('antman')  # remove 'antman' from the list
print(f"heros={heros}")

sugar_values = [1, 2, 3, 4, 5]
sugar_values.append(6)
print(f"sugar_values={sugar_values}")
sugar_values.insert(0, 0)
print(f"sugar_values={sugar_values}")
sugar_values.sort()
print(f"sorted_sugar_values={sugar_values}")
print(f"minimum suger={min(sugar_values)}")
sugar_values.pop()  # remove the last element
print(f"sugar_values={sugar_values}")
sugar_values.pop(0)  # remove the first element
print(f"sugar_values={sugar_values}")
print(f"maximum suger={max(sugar_values)}")


strong_brew = ['black coffee', 'espresso', 'americano'] * 3
print(f"strong_brew={strong_brew}")