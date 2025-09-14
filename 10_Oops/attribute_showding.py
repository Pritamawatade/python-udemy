class Chai:
    temp = "hot"

cutting = Chai()

print("before temp changes ", cutting.temp)
cutting.temp = "cold"
cutting.cup = "glass" # creation of new atttribute which does not exist in the calss
print(f"cup = {cutting.cup}")
print("after temp changes ", cutting.temp)
print("class  cutting  ", Chai.temp)
del cutting.temp
print("after deletion of cutting ", cutting.temp) # after deletion it fall back to previous value

# let's delete the cup which was added later and have no fallback value

del cutting.cup

print(f"cup = {cutting.cup}")

