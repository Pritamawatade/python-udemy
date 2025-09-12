def serve_chai():
    yield "chai 1"
    yield "chai 2"


one = serve_chai()
print(next(one)) # prints the next value form the iterator. The function resume where it is left 
print(f"type of object = {type(one)}")

for i  in one:
    print(i)
