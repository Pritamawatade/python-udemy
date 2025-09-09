def local_chai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "matchha"
    yield "oolong"


def menu():
    yield from local_chai()
    yield from imported_chai()



for i in menu():
    print(i)


# close the generator
# we use this when we want to close the generator
print("-------->closing the generator")
def close_gen():
    try:
        while(True):
            order = yield "waiting for order"
            print(f"order = {order}")
    except:
        print("stall closed")

chai = close_gen()
print(next(chai))
chai.send("masala")
chai.send("ginger")
chai.close()