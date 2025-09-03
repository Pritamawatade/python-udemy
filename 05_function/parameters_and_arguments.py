def chai(chai, milk, sugar):
    print(chai,milk,sugar)

chai("tulsi", "no", "yes") # This is callled positional aruguments since the position has to match with function defination
chai(chai="elaychi", sugar="no", milk="yes") # This is the keyword arguments, order doesn't matter here

def special_chai(*args, **kwargs):  # *args and **kwargs (keyword arguments) is just variable names and can be replaced with any other name
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


# def special_chai(*ingredients, **extras):
#     print(f"ingredients: {ingredients}")
#     print(f"kwargs: {extras}")

special_chai("tulsi", "no", "yes", chai="elaychi", sugar="no", milk="yes")


# def default_trap(order=[]): # This is a bad practice, because the default value is created only once and shared by all the calls.
#     order.append("tulsi")
#     return order

def default_trap(order=None): # This is a good practice, because the default value is created only once and shared by all the calls.
    if order is None:
        order = []
    order.append("tulsi")
    return order

print(default_trap())
print(default_trap())

# output: [tulsi] [tulsi]