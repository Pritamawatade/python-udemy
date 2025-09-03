def pure_function():
    total = 0
    total = 1_00_000
    print(f"pure function since it only work within itself {total}")


total = 500

def impure_function():
    global total 
    total = 1000
    print(f"impure function since it manupulates the global value  T = {total}")



# recursive function is like any other language

types = ['courages', 'intellectual','intellectual fool', 'survival', 'love']

#  lambda function without name
lamda = list(filter(lambda char: char == 'love', types))

print(lamda)
pure_function()
impure_function()