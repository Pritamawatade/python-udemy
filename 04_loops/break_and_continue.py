flavours = ["item0","item1", "item2", "discontinuedItem", "demo"]

for flavor in flavours:
    if  flavor == "item1":
        continue
    if flavor == "discontinuedItem":
        break   
    print(f"flavor = {flavor}")

print("outside of the loop")
